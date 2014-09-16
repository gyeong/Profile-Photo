# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash, jsonify
from werkzeug.security import generate_password_hash, \
     check_password_hash
from sqlalchemy import desc

from apps import app, db
from apps.forms import AdvertForm
from google.appengine.ext import db as gdb

from apps.models import (
    Advert
)


class Photo(gdb.Model):
	photo = gdb.BlobProperty()

def allowed_file(filename):
	ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

	return '.' in filename and \
	filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


 
@app.route('/')
def index():
	return render_template('home.html')

@app.route('/join')
def join():
	return render_template('join.html')

@app.route('/about')
def about():
	return render_template('about.html')






	
@app.route('/img_upload', methods=['GET', 'POST'])
def img_upload():
	if request.method == 'POST':

		post_data = request.files['photo']
		if post_data and allowed_file(post_data.filename):
			filestream = post_data.read()

			upload_data = Photo()
			upload_data.photo = gdb.Blob(filestream)
			upload_data.put()

			comment = "uploaded!"
			key = upload_data.key()
			# 여기서 키값을 저장합니다!!!!!!!!!!

			return redirect(url_for('upload', key=key)) 
	else:
		return render_template("img_upload.html")



@app.route('/upload/<key>', methods=['GET', 'POST'])
def upload(key):
	form = AdvertForm()

    	if request.method == 'POST':
        		if form.validate_on_submit():
		            # 사용자가 입력한 글 데이터로 Article 모델 인스턴스를 생성한다.
		            advert = Advert(
		                title=form.title.data,
		                author=form.author.data,
		                category=form.category.data,
		                content=form.content.data,
		                term = form.term.data,
		                reward = form.reward.data,
		                img_upload = key
		            )

		            # 데이터베이스에 데이터를 저장할 준비를 한다. (게시글)
		            db.session.add(advert)
		            # 데이터베이스에 저장하라는 명령을 한다.
		            db.session.commit()

		            flash(u'게시글을 작성하였습니다.', 'success')
		            return redirect(url_for('index'))

	return render_template('upload.html', form = form, active_tab='article_create')





