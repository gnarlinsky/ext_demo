The script `cover.sh` (in the `mysite` directory, on the same level as
`manage.py`) runs the tests (see :mod:`app.tests`) and determines test
coverage, with detailed HTML results.

.. code-block:: shell

    $ ./cover.sh 
    Creating test database for alias 'default'...

    TestCase AdminTests
    test_clean:  Test that if the Emails ('all_emails') field does not contain at
            least one valid email address, the correct error is returned.
            
    TestCase HelpersTests
    test_helpers: 
            Test that valid email addresses are parsed from string.
            
            Is empty string parsed correctly?
            Is a single non-email string parsed correctly?

            < . . . omitting output . . .  >

    ----------------------------------------------------------------------
    Ran 30 tests in 0.016s

    OK
    Destroying test database for alias 'default'...
    Name           Stmts   Miss  Cover   Missing
    --------------------------------------------
    app/__init__       0      0   100%   
    app/admin         29     11    62%   19-28, 68
    app/forms         19      0   100%   
    app/helpers        4      0   100%   
    app/models        26      0   100%   
    app/views         25     16    36%   13, 19-38
    --------------------------------------------
    TOTAL            103     27    74%   

    HTML results are in htmlcov/index.html


.. note::
    **Cover.sh** - The line ``open htmlcov/index.html`` opens the HTML
    coverage information with your system's default browser. Note this may only work
    in OS X, where the ``open`` command opens directories and files with the
    default application for the file's extension — so you might want to comment out
    that statement.

