# -*- coding: utf-8 -*-
from wtforms import Form, StringField
from wtforms.validators import Email


class EmailForm(Form):
    email = StringField('e-mail', validators=[Email()])

