from flask import render_template, request, redirect, url_for
from climbing_log import app, db



@app.route("/")
def home():
    return render_template("base.html")