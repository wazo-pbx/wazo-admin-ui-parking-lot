# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask_menu.classy import classy_menu_item
from marshmallow import fields

from wazo_admin_ui.helpers.classful import BaseView
from wazo_admin_ui.helpers.mallow import BaseSchema, BaseAggregatorSchema, extract_form_fields

from .form import ParkingLotForm


class ParkingLotSchema(BaseSchema):

    class Meta:
        fields = extract_form_fields(ParkingLotForm)


class ExtensionSchema(BaseSchema):
    context = fields.String(default='default')
    exten = fields.String(attribute='extension')


class AggregatorSchema(BaseAggregatorSchema):
    _main_resource = 'parking_lot'

    parking_lot = fields.Nested(ParkingLotSchema)
    extension = fields.Nested(ExtensionSchema)


class ParkingLotView(BaseView):

    form = ParkingLotForm
    resource = 'parking_lots'
    schema = AggregatorSchema

    @classy_menu_item('.parkinglots', 'Parking Lots', order=2, icon="automobile")
    def index(self):
        return super(ParkingLotView, self).index()

    def _map_resources_to_form(self, resources):
        schema = self.schema()
        data = schema.load(resources).data
        main_exten = schema.get_main_exten(resources['parking_lot'].get('extensions', {}))
        form = self.form(data=data['parking_lot'], extension=main_exten)
        moh_name = resources['parking_lot'].get('music_on_hold')
        form.music_on_hold.choices = [(moh_name, moh_name)]
        return form
