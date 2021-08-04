from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv

#Configuration of the database application
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SECRET_KEY']= str(os.urandom(16))

db = SQLAlchemy(app)

from . import routes