from flask import render_template, request, redirect, url_for
from climbing_log import app, db
from climbing_log.models import Users, Sessions, Climb



@app.route("/")
def home():
    return render_template("base.html")