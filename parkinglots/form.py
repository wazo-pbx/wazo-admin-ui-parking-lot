# -*- copyright 2017 by Sylvain Boily
# SPDX-License-Identifier: GPL-3.0+

from flask_wtf import FlaskForm

from wtforms.fields import SubmitField
from wtforms.fields import TextField
from wtforms.fields import IntegerField

from wtforms.validators import InputRequired
from wtforms.validators import Optional

class ParkingLotForm(FlaskForm):
    name = TextField('Name', [InputRequired()])
    extension = TextField('Extension', [InputRequired()])
    slots_start = TextField('Slots Start', [InputRequired()])
    slots_end = TextField('Slots End', [InputRequired()])
    music_on_hold = TextField('Music On Hold')
    timeout = IntegerField('Timeout', [Optional()])
    submit = SubmitField('Submit')
