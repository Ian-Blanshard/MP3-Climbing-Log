from flask import render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user
from climbing_log import app, db, login_manager
from climbing_log.models import Users, Sessions, Climb



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
        if user.password == request.form.get("password"):
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
        duplicate_user = Users.query.filter(
            (Users.username == user.username)).first()
        
        duplicate_email = Users.query.filter(
            (Users.email == user.email)).first()

        if duplicate_user:
            flash('duplicate username')
        elif duplicate_email:
            flash('duplicate email')
        else:
            db.session.add(user)
            db.session.commit()
        return redirect(url_for("add_user"))
    return render_template("add_user.html")