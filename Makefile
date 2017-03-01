install:
	python setup.py install
	cp etc/wazo-admin-ui/conf.d/parking_lot.yml /etc/wazo-admin-ui/conf.d
	systemctl restart wazo-admin-ui

uninstall:
	pip uninstall wazo-admin-ui-parking-lot
	rm /etc/wazo-admin-ui/conf.d/parking_lot.yml
	systemctl restart wazo-admin-ui
