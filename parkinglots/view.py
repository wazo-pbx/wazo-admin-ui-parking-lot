# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask_menu.classy import classy_menu_item

from wazo_admin_ui.helpers.classful import BaseView

from .form import ParkingLotForm


class ParkingLotsView(BaseView):

    form = ParkingLotForm
    resource = 'parking_lots'
    templates = {'list': 'parkinglots.html',
                 'edit': 'view_parkinglots.html'}

    @classy_menu_item('.parkinglots', 'Parking Lots', order=2, icon="automobile")
    def index(self):
        return super(ParkingLotsView, self).index()

    def _map_resources_to_form_get(self, parking_lot):
        main_exten = self._get_main_exten(parking_lot.get('extensions', {}))
        return self.form(data=parking_lot, extension=main_exten)

    def _get_main_exten(self, extensions):
        for extension in extensions:
            return extension['exten']
        return None

    def _map_form_to_resources_post(self, form):
        parking_lot = {
            'name': form.name.data,
            'slots_start': form.slots_start.data,
            'slots_end': form.slots_end.data,
            'music_on_hold': form.music_on_hold.data,
            'timeout': form.timeout.data
        }
        extension = {
            'exten': form.extension.data,
            'context': 'default'  # TODO: should be in the form
        }
        return parking_lot, extension

    def _map_form_to_resources_put(self, form, form_id):
        parking_lot, extension = self.map_form_to_resources_post(form)
        parking_lot['id'] = form_id
        parking_lot['slots_start'] = form.slots_start.data
        parking_lot['slots_end'] = form.slots_end.data
        parking_lot['music_on_hold'] = form.music_on_hold.data
        parking_lot['timeout'] = form.timeout.data
        return parking_lot, extension

    def _map_resources_to_form_errors(self, form, resources):
        parking_lot = resources.get('parking_lots')
        if parking_lot:
            if 'name' in parking_lot:
                form.name.errors.append(parking_lot['name'])
            if 'slots_start' in parking_lot:
                form.slots_start.errors.append(parking_lot['slots_start'])
            if 'slots_end' in parking_lot:
                form.slots_end.errors.append(parking_lot['slots_end'])
            if 'music_on_hold' in parking_lot:
                form.music_on_hold.errors.append(parking_lot['music_on_hold'])
            if 'timeout' in parking_lot:
                form.timeout.errors.append(parking_lot['timeout'])

        extension = resources.get('extensions')
        if extension:
            if 'exten' in extension:
                form.extension.errors.append(extension['exten'])

        return form
