Per two scoops books (but to reword and incorporate into gwiki or whatever handout or just to note to explain for the presenation)

``base.py``:
Settings common to all instances of the project.

``local.py``
This is the settings file that you use when you're working on the project locally. Local development-specific settings include DEBUG mode, log level, and activation of developer tools like django-debug-toolbar. Developers sometimes name this file dev.py.

``staging.py``
Staging version for running a semi-private version of the site on a production server. This is where managers and clients should be looking before your work is moved to production.

``test.py``
Settings for running tests including test runners, in-memory database definitions, and log settings.

``production.py``
This is the settings file used by your live production server(s). That is, the server(s) that host the real live website. This file contains production-level settings only. It is sometimes called prod.py.
