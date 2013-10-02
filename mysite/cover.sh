#!/usr/bin/env bash

#coverage run manage.py test app
coverage run manage.py test --settings=mysite_config_root.settings.test

#coverage report -m --include="app/*" --omit="app/misc.py,app/tests/*"

# don't report on django packages, or any other packages that aren't mine
coverage report -m --include="app/*" --omit="app/tests/*"
#coverage html --include="app/*" --omit="app/tests/*"
coverage html --include="app/*" --omit="app/tests/*"

# note: only os x
open htmlcov/index.html
