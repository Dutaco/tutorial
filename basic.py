import os
from typing import ContextManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

######################################
#### SET UP OUR SQLite DATABASE #####
####################################

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#####################################
####################################
###################################

# Let's create our first model!
# We inherit from db.Model class


class Course(db.Model):

    __tablename__ = 'courses'

    #########################################
    ## CREATE THE COLUMNS FOR THE TABLE ####
    #######################################

    # Primary Key column, unique id for each course
    id = db.Column(db.Integer, primary_key=True)
    # Course name
    name = db.Column(db.Text)
    # Course finished in percentages
    progress = db.Column(db.Integer)
    content = db.Column(db.Text)

    # This sets what an instance in this table will have
    # Note the id will be auto-created for us later, so we don't add it here!
    def __init__(self, name, progress, content):
        self.name = name
        self.progress = progress
        self.content = content

    def __repr__(self):
        # This is the string representation of a course in the model
        return f"Course {self.name} is {self.progress} percentages finished."
