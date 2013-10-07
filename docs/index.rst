.. demo documentation master file, created by
   sphinx-quickstart on Sun Feb 17 11:35:50 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.





Testing inserting images:
===============================
.. image:: test_image.png
   :width: 300 px

.. contents::


Setting up
======================================
<README.md goes here>

.. include:: ../README.rst
   (actually, change to readme.md, not rst)

Developer documentation
===============================

API
--------
.. toctree::
   :maxdepth: 4

   demo
   demo-other
   demo-tests
   temp_test

Internal documentation/design documents
-----------------------------------------------
So here go decisions like the schema, and stuff that didn't go into the
individual 'Internal documentation' parts of each py file

Scripts
---------------
Not sure where to put or categorize this...........
But here should talk about cover.sh

** ``Cover.sh`` ** - The line ``open htmlcov/index.html`` opens the HTML
coverage information with your system's default browser. But this may only work
in OS X, where the ``open`` command opens directories and files with the
default application for the file's extension — so you might want to comment out
that statement.

End user documentation
======================================
(Yes, this is silly for this project, but it's just a demo)


Administrative user documentation
======================================
FAQ
--------


Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
