.. demo documentation master file, created by Nadia Karlinsky


##########################
Demo App Documentation
##########################

.. toctree::
   :maxdepth: 6

   index

About
===============

Small demo of single-page web application with a contact form for customers
and an administrative interface for admin users to manage (display, search,
edit, delete) customers' information. The form for customers contains fields
for contact information. *Customers should be able to enter
multiple email addresses.*


Created with
=============================================================

Python/Django/SQLite (development version)

The front end  (customer contact information form) is responsively styled using
`Bootstrap <http://getbootstrap.com/>`_ and `Django Bootstrap Toolkit
<https://github.com/dyve/django-bootstrap-toolkit/>`_. The admin interface
(list of users, change form for individual users, login) is responsively styled
using `Bootstrap <http://getbootstrap.com/>`_ and `Django Suit
<http://djangosuit.com/>`_, with some customization.


Setting up and running the application
==========================================

Clone the repository.

.. code-block:: shell

    $ git clone git@github.com:gnarlinsky/ext_demo.git

To avoid dependency issues, create a virtualenv and install the required
packages.

Inside whereever you keep your virtualenv's:

.. code-block:: shell

    $ virtualenv ve --no-site-packages
    $ source ve/bin/activate      # activate the virtual environment

Install the requirements:

.. code-block:: shell

    $ cd ext_demo/mysite/
    $ pip install -r requirements.txt

Create the database and load the initial data:

.. code-block:: shell

    $ python manage.py syncdb
    $ python manage.py loaddata app/fixtures/initial.json

Run the Django development server:

.. code-block:: shell

    $ python manage.py runserver


Go to [http://localhost:8000/signup](http://localhost:8000/signup) to see
interface for customers,
or to [http://localhost:8000/admin](http://localhost:8000/signupadmin) to see the
administrative interface. Log in with username *homer* and password *homer*.

Note that `manage.py syncdb` creates a database, so if you would like to
start fresh, make sure to delete it. Assuming you're still in the same
directory (`ext_demo/mysite/`)::

    $ rm mysite_config_root/default.db


Developer documentation
===============================

API
--------
.. toctree::
   :maxdepth: 4

   demo
   demo-other
   demo-tests

Internal documentation/design notes
-----------------------------------------------

.. toctree::
   :maxdepth: 4

   internal_and_design




Testing and coverage
============================
.. include:: testing_and_coverage.rst

End user (administrative users) documentation
==================================================
.. include:: enduser_documentation.rst


Meta
=========
This documentation
---------------------
Documentation created with `Sphinx, a Python document generator
<http://sphinx-doc.org/>`_.


Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
