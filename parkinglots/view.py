# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask_menu.classy import classy_menu_item
from marshmallow import fields, post_load, pre_dump

from wazo_admin_ui.helpers.classful import BaseView
from wazo_admin_ui.helpers.mallow import BaseSchema

from .form import ParkingLotForm


class ParkingLotSchema(BaseSchema):

    class Meta:
        additional = ('name',
                      'slots_start',
                      'slots_end',
                      'music_on_hold',
                      'timeout')


class ExtensionSchema(BaseSchema):
    context = fields.String(default='default')
    exten = fields.String(attribute='extension')


class ParkingLotFormSchema(BaseSchema):
    _main_resource = 'parking_lot'

    parking_lot = fields.Nested(ParkingLotSchema)
    extension = fields.Nested(ExtensionSchema)

    @post_load(pass_original=True)
    def create_form(self, data, raw_data):
        main_exten = self.get_main_exten(raw_data['parking_lot'].get('extensions', {}))
        return ParkingLotForm(data=data['parking_lot'], extension=main_exten)

    @pre_dump
    def add_envelope(self, data):
        return {'parking_lot': data,
                'extension': data}


class ParkingLotsView(BaseView):

    form = ParkingLotForm
    resource = 'parking_lots'
    schema = ParkingLotFormSchema
    templates = {'list': 'parkinglots.html',
                 'edit': 'view_parkinglots.html'}

    @classy_menu_item('.parkinglots', 'Parking Lots', order=2, icon="automobile")
    def index(self):
        return super(ParkingLotsView, self).index()
