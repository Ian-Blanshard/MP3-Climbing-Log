from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from climbing_log import app, db, login_manager, bcrypt
from climbing_log.models import Users, Sessions, Climb
from datetime import datetime




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
        is_valid = bcrypt.check_password_hash(user.password, request.form.get("password"))
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
            user.password = bcrypt.generate_password_hash(user.password).decode('utf-8')
            db.session.add(user)
            db.session.commit()
        return redirect(url_for("login"))
    return render_template("add_user.html")

@app.route("/add_session", methods=["GET", "POST"])
def add_session():
    if request.method == 'POST':
        # get current date/time
        now = datetime.now()

        session = Sessions(
            user_id = current_user.user_id,
            date = now.date(),
            location = request.form.get('location'),
            # session length will be calculated when last climb is logged
            length = 0,
            time = now
        )

        db.session.add(session)
        db.session.commit()


    return render_template('session_info.html')