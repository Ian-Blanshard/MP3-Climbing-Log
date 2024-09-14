from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from climbing_log import app, db, login_manager, bcrypt
from climbing_log.models import Users, Sessions, Climb
from datetime import datetime, date
from sqlalchemy.orm import joinedload
from climbing_log.chart_queries import (
    get_completed_uncompleted_climbs,
    get_range_of_difficulty_climbed,
    get_range_of_length_climbs,
    get_range_of_difficulty_not_climbed
)


@app.route("/")
def home():
    """returns home page, if user is authenticated also returns 10 most recent
        sessions"""
    # if user is logged in
    if current_user.is_authenticated:
        # query database for 10 most recent sessions
        sessions = (
            Sessions.query
            .options(joinedload(Sessions.climbs))
            .filter_by(user_id=current_user.user_id)
            .order_by(Sessions.session_id.desc())
            .limit(10)
            .all()
        )
        # return homepage with sessions
        return render_template("home.html", sessions=sessions)
    # user not logged in return homepage
    return render_template('home.html')


@login_manager.user_loader
def loader_user(user_id):
    """returns user from database, this is used by flask-login for session
    managment"""
    return Users.query.get(user_id)


@app.route("/login", methods=["GET", "POST"])
def login():
    """handles the user form for logging in using GET/POST, GET will present
    login form to user, POST will deal with user submiting form and check
    validity of password with bcrypt, flashed messages for user info"""
    # If a post request was made, find the user by
    # filtering for the username
    if request.method == "POST":
        user = Users.query.filter_by(
            username=request.form.get("username")).first()
        # Check if the password entered is the
        # same as the user's password
        if user:
            # get hashed password from database and check is same as entered
            # password
            is_valid = bcrypt.check_password_hash(
                user.password, request.form.get("password"))
            if is_valid:
                # Use the login_user method to log in the user
                login_user(user)
                # alert user they are logged in
                flash('You are now logged in')
                # take them to homepage
                return redirect(url_for("home"))
            else:
                # if incorrect password alert users
                flash('Password incorrect please re-enter')
        else:
            # if user enters username which is not in database alert them
            flash('There is no user by this name, check you entered your '
                  'username correctly or create a new account')
        # Redirect the user back to the home
    # if GET request render login page
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    """log user out, flashes message for user info and returns homepage"""
    # log user out
    logout_user()
    # alert user they are logged out
    flash('You are logged out')
    # redirect user to homepage
    return redirect(url_for("home"))


@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    """handles the user form for creating account using GET/POST,
    GET will present add user form to user, POST will deal with user
    submiting form and check validity of details added, bcrypt will hash
     password before sending to database, flashed messages for user info"""
    today = date.today().strftime('%Y-%m-%d')
    # if POST request / user submitting for
    if request.method == 'POST':
        # get info submitted and save to user varaiable
        user = Users(username=request.form.get('username'),
                     email=request.form.get('email'),
                     password=request.form.get('password'),
                     date_of_birth=request.form.get('date_of_birth'),
                     sex=request.form.get('sex'),
                     height=request.form.get('height'),
                     weight=request.form.get('weight'))
        password_check = request.form.get('password_check')
        # check if username already exists in database
        duplicate_user = Users.query.filter(
            (Users.username == user.username)).first()
        # check if email already exists in database
        duplicate_email = Users.query.filter(
            (Users.email == user.email)).first()
        # flash messages to alert user if duplicates exist
        if duplicate_user:
            flash('duplicate username')
        elif duplicate_email:
            flash('duplicate email')
        # flash message to alert user if passwords entered don't match
        elif user.password != password_check:
            flash('passwords do not match')
            return render_template("add_user.html")
        # if all entrys ok hash password
        else:
            user.password = bcrypt.generate_password_hash(
                user.password).decode('utf-8')
            # add/commit details to database
            db.session.add(user)
            db.session.commit()
            # alert user on successful account creation
            flash('User account created')
        # take user to login page
        return redirect(url_for("login"))
    # GET request loads add user page/frm
    return render_template("add_user.html", max_date=today)


@app.route("/delete_user", methods=["GET", "POST"])
@login_required
def delete_user():
    """handles the user form for deleting account using GET/POST,
    GET will present delete user form to user, POST will deal with user
    submiting form and check password entered twice is the same and matches
    hashed password in database, flashed messages for user info"""
    # if from submitted
    if request.method == 'POST':
        # get current username details from database
        user = Users.query.filter_by(
            username=current_user.username).first()
        # get passwords entered from form
        password = request.form.get('password')
        password_check = request.form.get('password_check')
        # check both password match
        if password != password_check:
            # if don't match alert user
            flash('passwords do not match')
        # if do match check that password matches hashed one in database
        else:
            is_valid = bcrypt.check_password_hash(
                user.password, password)
            # if does match delete user and commit change to database
            if is_valid:
                db.session.delete(user)
                db.session.commit()
                # alert user deletion was succesful
                flash('User account deleted')
                # redirect to homepage
                return redirect(url_for('home'))
            else:
                # if password doesnt match database alert user
                flash('Password incorrect')
    # GET request returns delete user form
    return render_template('delete_user.html')


@app.route("/new_session", methods=["GET", "POST"])
@login_required
def add_session():
    """handles the user form for creating new session using GET/POST,
    GET will present new session form to user, POST will deal with user
    submiting form and create new session for that user, flashed messages
    for user info"""
    # POST request deals with user submitting new session form
    if request.method == 'POST':
        # get current date/time, used for calculating session length
        now = datetime.now()
        # create session variable
        session = Sessions(
            user_id=current_user.user_id,
            date=now.date(),
            location=request.form.get('location'),
            # session length will be calculated when last climb is logged
            length=0,
            time=now
        )
        # add new session to database and commit changes
        db.session.add(session)
        db.session.commit()
        # alert user new session was created
        flash('New session created')
        # redirect user to log climb page for this session
        return redirect(url_for("log_climb"))
    # GET request returns new session form
    return render_template('new_session.html')


@app.route("/log_climb", methods=["GET", "POST"])
@login_required
def log_climb():
    """handles the user form for logging a climb using GET/POST, GET will
    present log climb form to user, POST will deal with user submiting form
    and add new climb details to database for current session
    , flashed messages for user info"""
    # POST request deals with form submission
    if request.method == 'POST':
        # gets current session from database to add climb to this
        current_session = Sessions.query.filter_by(
            user_id=current_user.user_id).order_by(Sessions.time.desc()
                                                   ).first()
        # so code works if first session and no session to find in database
        if not current_session:
            current_session = 0
        # create climb variable from form
        climb = Climb(
            session_id=current_session.session_id,
            difficulty=request.form.get('difficulty'),
            length=int(request.form.get('length')),
            name=request.form.get('name'),
            completed=(request.form.get('completed') == 'True')
        )
        # this climb time when logged
        last_climb_time = datetime.now()
        # start of session climb time
        first_climb_time = current_session.time
        # difference between the two = length of sesssion
        session_length = last_climb_time - first_climb_time
        # change to correct value for database (seconds)
        session_length_in_seconds = session_length.total_seconds()
        current_session.length = session_length_in_seconds
        # add climb to database and commit changes
        db.session.add(climb)
        db.session.commit()
        # alert user that climb was logged
        flash('Climb logged')

        if request.form.get('action') == 'log_and_redirect':
            return redirect(url_for("sessions"))
        else:
            return redirect(url_for("log_climb"))
    # GET request returns log climb form
    return render_template('log_climb.html')


@app.route('/end_session')
@login_required
def end_session():
    """for user to end current session from log climb page"""
    # alert user session is ended
    flash('Session logged')
    # redirect them to sessions page
    return redirect(url_for('sessions'))


@app.route("/session_info/<int:session_id>")
@login_required
def session_info(session_id):
    """Displays page and creates plotly charts from session_id passed"""
    # if current user is logged in pass session id to methods for charts
    if current_user.is_authenticated:
        pie_json = get_completed_uncompleted_climbs(session_id)
        bar_json = get_range_of_difficulty_climbed(session_id)
        bar_uncompleted_grades = get_range_of_difficulty_not_climbed(
            session_id)
        scatter_json = get_range_of_length_climbs(session_id)
        # return page and JSON represntations of plotly charts
        return render_template(
            'session_info.html',
            graphJSON=pie_json,
            graph1JSON=bar_json,
            graph_grades_not_climbedJSON=bar_uncompleted_grades,
            scatterJSON=scatter_json
        )
    # render session info without charts JSONs
    return render_template('session_info.html')


@app.route("/edit_climb/<int:climb_id>", methods=["GET", "POST"])
@login_required
def edit_climb(climb_id):
    """handles the user form for editing a climb using GET/POST, GET will
    present edit climb form to user filling in the climb details for the passed
    id, POST will deal with user submiting form and update climb details
    , flashed messages for user info"""
    # query database for climb details to fill form
    climb = Climb.query.get_or_404(climb_id)
    # if POST get details from form
    if request.method == "POST":
        climb.name = request.form.get('name')
        climb.difficulty = request.form.get('difficulty')
        climb.length = request.form.get('length')
        climb.completed = request.form.get('completed') == 'True'
        # commit changes to db
        db.session.commit()
        # alert user changes successful
        flash('Climb updated')
        return redirect(url_for("sessions"))
    # render page with climb details
    return render_template("edit_climb.html", climb=climb, climb_id=climb_id)


@app.route("/delete_climb/<int:climb_id>", methods=["GET", "POST"])
@login_required
def delete_climb(climb_id):
    """deals with deletion of climbs from database"""
    # get climb from db for passed climb id
    climb = Climb.query.get_or_404(climb_id)
    # delete from db and commit changes
    db.session.delete(climb)
    db.session.commit()
    # alert user
    flash('Climb deleted')
    # redirect to sessions page
    return redirect(url_for("sessions"))


@app.route("/delete_session/<int:session_id>", methods=["GET", "POST"])
@login_required
def delete_session(session_id):
    """deals with deletion of sessions from database"""
    # get session from db for passed session id
    session = Sessions.query.get_or_404(session_id)
    # delete from db and commit changes
    db.session.delete(session)
    db.session.commit()
    # alert user
    flash('Session deleted')
    # redirect to sessions page
    return redirect(url_for("sessions"))


@app.route('/sessions')
@login_required
def sessions():
    """returns sessions page, contains logged in users sessions and
    climbs from these sessions """
    if current_user.is_authenticated:
        # query database for all sessions from user which is logged in
        # plus all the climbs from the sessions using the joinedload
        sessions = Sessions.query.options(
            joinedload(Sessions.climbs)).filter_by(
                user_id=current_user.user_id).order_by(
                    Sessions.session_id.desc()).all()
        # empty dictionary to hold session lengths
        session_lengths = {}
        # loop through all the sessions for user
        for session in sessions:
            session_length_in_seconds = session.length
            # calculate session minutes
            session_minutes = int(session_length_in_seconds // 60)
            # calculate remaining seconds
            session_seconds = int(session_length_in_seconds % 60)
            # calculate session in hours
            session_hours = int(session_minutes // 60)
            # calculate remaining minutes
            session_minutes = int(session_minutes % 60)
            # store result as string in dictionary
            session_lengths[session.session_id] = f'{session_hours} hours {
                session_minutes} mins {session_seconds} secs'

    # return template with current logged in user session history
    return render_template(
        'sessions.html', sessions=sessions, session_lengths=session_lengths)


@app.errorhandler(404)
def page_not_found(e):
    """displays 404 page"""

    return render_template('404.html'), 404

@app.errorhandler(401)
def unauthorized_error(e):
    """Displays 401 page, if user not logged in and attempts to access
    page that requires login"""
    return render_template('401.html'), 401
