from flask import render_template, request, redirect, url_for, flash
from climbing_log import app, db
from climbing_log.models import Users, Sessions, Climb



@app.route("/")
def home():
    return render_template("home.html")



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