# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import (
    StringField,
    PasswordField,
    TextAreaField
)
from wtforms import validators
from wtforms.fields.html5 import EmailField

class AdvertForm(Form):
    title = StringField(
        u'제목',
        [validators.data_required(u'제목을 입력하시기 바랍니다.')],
        description={'placeholder': u'제목을 입력하세요.'}
    )
    content = TextAreaField(
        u'내용',
        [validators.data_required(u'내용을 입력하시기 바랍니다.')],
        description={'placeholder': u'내용을 입력하세요.'}
    )
    author = StringField(
        u'작성자',
        [validators.data_required(u'이름을 입력하시기 바랍니다.')],
        description={'placeholder': u'이름을 입력하세요.'}
    )
    category = StringField(
        u'카테고리',
        [validators.data_required(u'카테고리를 입력하시기 바랍니다.')],
        description={'placeholder': u'카테고리를 입력하세요.'}
    )
    term = StringField(
        u'기간',
        [validators.data_required(u'기간을 입력하시기 바랍니다.')],
        description={'placeholder': u'기간을 입력하세요.'}
    )
    reward = StringField(
        u'리워드',
        [validators.data_required(u'리워드를 입력하시기 바랍니다.')],
        description={'placeholder': u'리워드를 입력하세요.'}
    )



