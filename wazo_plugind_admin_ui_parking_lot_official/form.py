# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wtforms.fields import (SubmitField,
                            StringField,
                            SelectField,
                            FieldList,
                            FormField)
from wtforms.fields.html5 import IntegerField
from wtforms.validators import InputRequired, NumberRange, Length, Regexp

from wazo_admin_ui.helpers.form import BaseForm


class ExtensionForm(BaseForm):
    exten = StringField('Extension', validators=[InputRequired()])
    context = SelectField('Context', validators=[InputRequired()])


class ParkingLotForm(BaseForm):
    name = StringField('Name', [InputRequired(), Length(max=128)])
    extensions = FieldList(FormField(ExtensionForm), min_entries=1)
    slots_start = StringField('Slots Start', [InputRequired(), Regexp(r'^[0-9]+$'), Length(max=40)])
    slots_end = StringField('Slots End', [InputRequired(), Regexp(r'^[0-9]+$'), Length(max=40)])
    music_on_hold = SelectField('Music On Hold', [Length(max=128)], choices=[])
    timeout = IntegerField('Timeout', [NumberRange(min=0)])
    submit = SubmitField('Submit')
