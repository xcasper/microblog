#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Craig
#
# Created:     17/03/2014
# Copyright:   (c) Craig 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!flask/bin/python
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

vars = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)
print 'Current database version: ' + str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO))
