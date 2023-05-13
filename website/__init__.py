# Author: Blanche Chung
# Created Date: Spring 2023
# Description: This file is the init file for the website package. It creates the flask app and the database.

from flask import Flask, render_template, request, redirect, url_for, send_file
from os import path
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager
from sqlalchemy import create_engine
import mysql.connector


db = SQLAlchemy()
DB_NAME = "notary_db"

#login_manager = LoginManager()


# define create_app function
def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='assets')
    app.config['SECRET_KEY'] = 'nvkfdljghkl;rfkd ghjp;lsgoi;'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://root:11236@localhost:3306/{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)
    #login_manager.init_app(app)

    # Set up the login view
    #login_manager.login_view = 'auth.login'

    # Import and register blueprints
    from .views import views

    app.register_blueprint(views, url_prefix='/')

    # Import remaining models
    from .models import User #, Notary

    # Check if database exists and create it if not
    with app.app_context():
        engine = create_engine(f'mysql+mysqlconnector://root:11236@localhost:3306/')
        conn = engine.connect()

        # Check if the notary database exists
        result = conn.execute("SHOW DATABASES LIKE 'notary_db';")
        exists = result.fetchone()

        # If notary database doesn't exist, create it
        if not exists:
            conn.execute("CREATE DATABASE notary_db;")

        conn.execute(f"USE {DB_NAME};")
        db.app = app  # Bind the app to the db instance
        db.create_all()

    return app
