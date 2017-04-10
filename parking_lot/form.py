# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wtforms.fields import (SubmitField,
                            StringField,
                            SelectField,
                            FieldList,
                            FormField,
                            IntegerField)
from wtforms.validators import InputRequired, Optional

from wazo_admin_ui.helpers.form import BaseForm


class ExtensionForm(BaseForm):
    exten = StringField('Extension')
    context = StringField(default='default')


class ParkingLotForm(BaseForm):
    name = StringField('Name', [InputRequired()])
    extensions = FieldList(FormField(ExtensionForm), min_entries=1)
    slots_start = StringField('Slots Start', [InputRequired()])
    slots_end = StringField('Slots End', [InputRequired()])
    music_on_hold = SelectField('Music On Hold', choices=[])
    timeout = IntegerField('Timeout', [Optional()])
    submit = SubmitField('Submit')
