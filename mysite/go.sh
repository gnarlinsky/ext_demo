rm -f mysite_config_root/default.db ; ./manage.py syncdb; ./manage.py loaddata app/fixtures/initial.json; ./manage.py runserver
