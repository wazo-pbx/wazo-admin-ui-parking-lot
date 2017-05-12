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

    def _populate_form(self, form):
        form.music_on_hold.choices = self._build_setted_choices_moh(form)
        for form_extension in form.extensions:
            form_extension.context.choices = self._build_setted_choices_context(form_extension)
        return form

    def _build_setted_choices_moh(self, form):
        if not form.music_on_hold.data or form.music_on_hold.data == 'None':
            return []
        return [(form.music_on_hold.data, form.music_on_hold.data)]

    def _build_setted_choices_context(self, form):
        if not form.context.data or form.context.data == 'None':
            return []
        return [(form.context.data, form.context.data)]

    def _map_resources_to_form_errors(self, form, resources):
        form.populate_errors(resources.get('parking_lot', {}))
        form.extensions[0].populate_errors(resources.get('extension', {}))
        return form
