# -*- coding: utf-8 -*-
# Copyright 2017 by Sylvain Boily
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.service import BaseConfdService


class ParkingLotsService(BaseConfdService):

    resource = 'parking_lot'
    confd_resource = 'parking_lots'

    def update(self, resources):
        parking_lot = resources.get('parking_lot')
        extension = resources.get('extension')

        existing_extension = self._get_main_extension(parking_lot['id'])

        self._confd.parking_lots.update(parking_lot)

        if not extension:
            return

        if extension['exten'] and existing_extension:
            self._update_extension(existing_extension, extension)
        elif extension['exten']:
            self._add_extension(parking_lot['id'], extension)
        elif not extension['exten'] and existing_extension:
            self._remove_extension(parking_lot['id'], extension['id'])

    def _get_main_extension(self, parking_lot_id):
        for extension in self._confd.parking_lots.get(parking_lot_id)['extensions']:
            return extension
        return None

    def create(self, resources):
        parking_lot = resources.get('parking_lot')
        extension = resources.get('extension')

        parking_lot = self._confd.parking_lots.create(parking_lot)
        if parking_lot and extension:
            self._add_extension(parking_lot['id'], extension)

    def delete(self, parking_lot_id):
        parking_lot = self._confd.parking_lots.get(parking_lot_id)
        for extension in parking_lot['extensions']:
            self._remove_extension(parking_lot_id, extension['id'])
        self._confd.parking_lots.delete(parking_lot_id)

    def _update_extension(self, existing_extension, extension):
        if existing_extension['exten'] == extension['exten']:
            return

        extension['id'] = existing_extension['id']
        self._confd.extensions.update(extension)

    def _add_extension(self, parking_lot_id, extension):
        extension = self._confd.extensions.create(extension)
        if extension:
            self._confd.parking_lots(parking_lot_id).add_extension(extension)

    def _remove_extension(self, parking_lot_id, extension_id):
        self._confd.parking_lots(parking_lot_id).remove_extension(extension_id)
        self._confd.extensions.delete(extension_id)
