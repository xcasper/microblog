#-------------------------------------------------------------------------------
# Name:        microblog
# Purpose:
#
# Author:      Craig
#
# Created:     15/03/2014
# Copyright:   (c) Craig 2014
# Licence:     None
#-------------------------------------------------------------------------------

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

#must be here because app is defined above
from app import views, models
