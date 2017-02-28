# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask import Blueprint
from flask_menu.classy import register_flaskview


from .service import ParkingLotService
from .view import ParkingLotView

parking_lot = Blueprint('parkinglots', __name__, template_folder='templates',
                        static_folder='static', static_url_path='/%s' % __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']
        config = dependencies['config']

        ParkingLotView.service = ParkingLotService(config['confd'])
        ParkingLotView.register(parking_lot, route_base='/parkinglots')
        register_flaskview(parking_lot, ParkingLotView)

        core.register_blueprint(parking_lot)
