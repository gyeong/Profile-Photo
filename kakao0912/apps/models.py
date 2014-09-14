"""
models.py
"""
from flask import Flask
r
from apps import app, pdb
from google.appengine.ext import db 

#
# add User Model
#
class Advert(pdb.Model):
	id = pdb.Column(pdb.Integer, primary_key=True)
	title = pdb.Column(pdb.String(255))
	content = pdb.Column(pdb.Text())
	author = pdb.Column(pdb.String(255))
	category = pdb.Column(pdb.String(255))
	term = pdb.Column(pdb.String(255))
	reward = pdb.Column(pdb.String(255))
	img_upload = pdb.Column(pdb.String(255))

	date_created = pdb.Column(pdb.DateTime(), default=pdb.func.now())


class Photo(pdb.Model):
	__tablename__ = 'Photo'
	photo = db.BlobProperty(primary_key=True)
