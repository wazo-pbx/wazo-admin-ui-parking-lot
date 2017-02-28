# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import unittest
from mock import Mock, patch

from hamcrest import assert_that, contains, equal_to, has_entries, has_properties

from ..form import ParkingLotForm
from ..view import ParkingLotFormSchema


class TestSchemas(unittest.TestCase):

    @patch('wazo_admin_ui.plugins.parkinglots.view.ParkingLotForm')
    def test_parking_lot_form_schema_load(self, parking_lot_form):
        resources = {'parking_lot': {'name': 'parking_1',
                                     'extensions': [{'exten': '1234'}]}}

        ParkingLotFormSchema().load(resources).data
        form = parking_lot_form.call_args[1]

        expected_call = {'data': {'name': 'parking_1'},
                         'extension': '1234'}
        assert_that(form, equal_to(expected_call))

    def test_parking_lot_form_schema_dump(self):
        # Do not use attribute name with Mock, it's reserved ...
        form = Mock(ParkingLotForm,
                    music_on_hold=Mock(data='music'),
                    extension=Mock(data='1234'))

        resources = ParkingLotFormSchema().dump(form).data

        assert_that(resources, has_entries(parking_lot=has_entries(music_on_hold='music'),
                                           extension=has_entries(exten='1234',
                                                                 context='default')))

    def test_parking_lot_form_schema_populate_form_error(self):
        form = Mock(ParkingLotForm,
                    music_on_hold=Mock(errors=[]),
                    extension=Mock(errors=[]))

        resources_errors = {'parking_lot': {'music_on_hold': 'invalid length'},
                            'extension': {'exten': 'not in range'}}
        form = ParkingLotFormSchema().populate_form_errors(form, resources_errors)

        assert_that(form, has_properties(
            music_on_hold=has_properties(errors=contains('invalid length')),
            extension=has_properties(errors=contains('not in range')),
        ))
