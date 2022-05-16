
from flask import Flask
from flask_wtf.csrf import CSRFProtect

from flask_sqlalchemy import SQLAlchemy



#instantiate an object of Flask app
app = Flask(__name__, instance_relative_config=True)
csrf=CSRFProtect(app)

#Load the config file
from shopifytestapp import config
app.config.from_object(config.ProductionConfig)
app.config.from_pyfile('config.py', silent=False) #this is the config in instance folders

#database connection
db=SQLAlchemy(app)

#load your routes here
from shopifytestapp.routes import userroutes #since routes is now a module on its own

#load models
from shopifytestapp import models

