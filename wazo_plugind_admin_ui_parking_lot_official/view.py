# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask_menu.classy import classy_menu_item

from wazo_admin_ui.helpers.classful import BaseView

from .form import ParkingLotForm


class ParkingLotView(BaseView):

    form = ParkingLotForm
    resource = 'parking_lots'

    @classy_menu_item('.parkinglots', 'Parking Lots', order=2, icon="automobile")
    def index(self):
        return super(ParkingLotView, self).index()

    def _map_resources_to_form(self, resource):
        form = self.form(data=resource)
        moh_name = resource.get('music_on_hold')
        form.music_on_hold.choices = [(moh_name, moh_name)]
        return form

    def _map_resources_to_form_errors(self, form, resources):
        form.populate_errors(resources.get('parking_lot', {}))
        form.extensions[0].populate_errors(resources.get('extension', {}))
        return form
