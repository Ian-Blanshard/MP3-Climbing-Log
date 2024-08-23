from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from climbing_log import app, db, login_manager, bcrypt
from climbing_log.models import Users, Sessions, Climb
from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import joinedload
import pandas as pd
import json
from plotly.utils import PlotlyJSONEncoder
import plotly.express as px


@app.route("/")
def home():
    return render_template("home.html")

# Creates a user loader callback that returns the user object given an id


@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)


@app.route("/login", methods=["GET", "POST"])
def login():
    # If a post request was made, find the user by
    # filtering for the username
    if request.method == "POST":
        user = Users.query.filter_by(
            username=request.form.get("username")).first()
        # Check if the password entered is the
        # same as the user's password
        is_valid = bcrypt.check_password_hash(
            user.password, request.form.get("password"))
        if is_valid:
            # Use the login_user method to log in the user
            login_user(user)
            return redirect(url_for("home"))
        # Redirect the user back to the home

    return render_template("login.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == 'POST':
        user = Users(username=request.form.get('username'),
                     email=request.form.get('email'),
                     password=request.form.get('password'),
                     date_of_birth=request.form.get('date_of_birth'),
                     sex=request.form.get('sex'),
                     height=request.form.get('height'),
                     weight=request.form.get('weight'))
        password_check = request.form.get('password_check')

        duplicate_user = Users.query.filter(
            (Users.username == user.username)).first()

        duplicate_email = Users.query.filter(
            (Users.email == user.email)).first()

        if duplicate_user:
            flash('duplicate username')
        elif duplicate_email:
            flash('duplicate email')
        elif user.password != password_check:
            flash('passwords do not match')
        else:
            user.password = bcrypt.generate_password_hash(
                user.password).decode('utf-8')
            db.session.add(user)
            db.session.commit()
        return redirect(url_for("login"))
    return render_template("add_user.html")


@app.route("/new_session", methods=["GET", "POST"])
def add_session():
    if request.method == 'POST':
        # get current date/time
        now = datetime.now()

        session = Sessions(
            user_id=current_user.user_id,
            date=now.date(),
            location=request.form.get('location'),
            # session length will be calculated when last climb is logged
            length=0,
            time=now
        )
        db.session.add(session)
        db.session.commit()
        return redirect(url_for("log_climb"))
    return render_template('new_session.html')


@app.route("/log_climb", methods=["GET", "POST"])
def log_climb():
    if request.method == 'POST':
        current_session = Sessions.query.filter_by(
            user_id=current_user.user_id).order_by(Sessions.time.desc()).first()
        if not current_session:
            current_session = 0

        climb = Climb(
            session_id=current_session.session_id,
            difficulty=request.form.get('difficulty'),
            length=int(request.form.get('length')),
            name=request.form.get('name'),
            completed=(request.form.get('completed') == 'True')
        )
        db.session.add(climb)
        db.session.commit()
        return redirect(url_for("log_climb"))

    return render_template('log_climb.html')


@app.route("/session_info")
def session_info():
    if current_user.is_authenticated:
        # get data from database for chart
        # get the most recent session
        last_session = Sessions.query.filter_by(
            user_id=current_user.user_id).order_by(Sessions.session_id.desc()).first()
        # get number of climbs completed from most recent session
        completed_count = db.session.query(func.count(Climb.climb_id)).filter_by(
            session_id=last_session, completed=True).scalar()
        # get number of climbs not completed from most recent session
        not_completed_count = db.session.query(func.count(Climb.climb_id)).filter_by(
            session_id=last_session, completed=False).scalar()
        # use pandas to create the dataframe
        df = pd.DataFrame({
            'Status': ['Climbs completed', 'Climbs NOT completed'],
            'Amount': [completed_count, not_completed_count]
        })
        # use plotly to create the pie chart using the dataframe
        fig = px.pie(df, names='Status', values='Amount')
        # convert the plotly figure to JSON
        pie_json = json.dumps(fig, cls=PlotlyJSONEncoder)

        return render_template('session_info.html', graphJSON=pie_json)

    return render_template('session_info.html')


@app.route("/edit_climb/<int:climb_id>", methods=["GET", "POST"])
def edit_climb(climb_id):
    climb = Climb.query.get_or_404(climb_id)
    if request.method == "POST":
        climb.name = request.form.get('name')
        climb.difficulty = request.form.get('difficulty')
        climb.length = request.form.get('length')
        climb.completed = request.form.get('completed') == 'True'
        db.session.commit()
        return redirect(url_for("sessions"))
    return render_template("edit_climb.html", climb=climb, climb_id=climb_id)


@app.route("/delete_climb/<int:climb_id>")
def delete_climb(climb_id):
    climb = Climb.query.get_or_404(climb_id)
    db.session.delete(climb)
    db.session.commit()
    return redirect(url_for("sessions"))

@app.route("/delete_session/<int:session_id>")
def delete_session(session_id):
    session = Sessions.query.get_or_404(session_id)
    db.session.delete(session)
    db.session.commit()
    return redirect(url_for("sessions"))


@app.route('/sessions')
def sessions():
    if current_user.is_authenticated:
        # query database for all sessions from user which is logged in
        # plus all the climbs from the sessions using the joinedload
        sessions = Sessions.query.options(joinedload(Sessions.climbs)).filter_by(
            user_id=current_user.user_id).order_by(Sessions.session_id.desc()).all()

    # return template with current logged in user session history
    return render_template('sessions.html', sessions=sessions)
