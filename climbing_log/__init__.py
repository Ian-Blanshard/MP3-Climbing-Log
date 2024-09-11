import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
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

# create a Bcrypt object
bcrypt = Bcrypt(app)

# initialise flask-sqlalchemy extension
db = SQLAlchemy(app)

# LoginManager is need to be able to log users in and out
login_manager = LoginManager()
login_manager.init_app(app)

# flask migrate to be used to update the database
migrate = Migrate(app, db)

from climbing_log import routes
