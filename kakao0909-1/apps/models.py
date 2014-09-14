"""
models.py

"""
from apps import db

#
# add User Model
#
class Advert(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255))
	content = db.Column(db.Text())
	author = db.Column(db.String(255))
	category = db.Column(db.String(255))
	term = db.Column(db.String(255))
	reward = db.Column(db.String(255))
	img_upload = db.Column(db.String(255))

	date_created = db.Column(db.DateTime(), default=db.func.now())


