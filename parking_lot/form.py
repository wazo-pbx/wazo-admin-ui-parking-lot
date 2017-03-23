# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_wtf import FlaskForm

from wtforms.fields import SubmitField
from wtforms.fields import StringField
from wtforms.fields import IntegerField

from wtforms.validators import InputRequired
from wtforms.validators import Optional


class ParkingLotForm(FlaskForm):
    name = StringField('Name', [InputRequired()])
    extension = StringField('Extension', [InputRequired()])
    slots_start = StringField('Slots Start', [InputRequired()])
    slots_end = StringField('Slots End', [InputRequired()])
    music_on_hold = StringField('Music On Hold')
    timeout = IntegerField('Timeout', [Optional()])
    submit = SubmitField('Submit')
