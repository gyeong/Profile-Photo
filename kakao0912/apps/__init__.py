from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager

app = Flask('apps')
app.config.from_object('apps.settings.Production')


pdb = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, pdb)
manager.add_command('db', MigrateCommand)

import views, models