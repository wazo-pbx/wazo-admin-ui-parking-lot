# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask import Blueprint
from flask_menu.classy import register_flaskview


from .service import ParkingLotsService
from .view import ParkingLotsView

parkinglots = Blueprint('parkinglots', __name__, template_folder='templates',
                        static_folder='static', static_url_path='/%s' % __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']
        config = dependencies['config']

        ParkingLotsView.service = ParkingLotsService(config['confd'])
        ParkingLotsView.register(parkinglots, route_base='/parkinglots')
        register_flaskview(parkinglots, ParkingLotsView)

        core.register_blueprint(parkinglots)
