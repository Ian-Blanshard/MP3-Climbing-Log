import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
if os.path.exists("env.py"):
    import env

# create the flask application
app = Flask(__name__)

# get secret key stored elsewhere for security
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# tell flask-sqlalchemy what database to connect to
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

# initialise flask-sqlalchemy extension
db = SQLAlchemy(app)

# LoginManager is need to be able to log users in and out
login_manager = LoginManager()
login_manager.init_app(app)

from climbing_log import routes