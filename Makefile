install:
	python setup.py install
	cp etc/wazo-admin-ui/conf.d/parkinglots.yml /etc/wazo-admin-ui/conf.d
	systemctl restart wazo-admin-ui

uninstall:
	pip uninstall wazo-admin-ui-parking-lots
	rm /etc/wazo-admin-ui/conf.d/parkinglots.yml
	systemctl restart wazo-admin-ui
