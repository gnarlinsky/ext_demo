from django.test import TestCase
from app.helpers import parse_emails
from ttools import t_info

class HelpersTests(TestCase):
    def setUp(self):
        t_info("TestCase HelpersTests", 1)
        t_info(self._testMethodName + ": " + self._testMethodDoc, 3)

# TODO: these are just copied from elsewhere, so complete
    def test_helpers(self):
        """
        Test that valid email addresses are parsed from string.
        """
        input_string = ''
        correct_out = []
        self.assertEqual(parse_emails(input_string), correct_out)

        input_string = 'alskjfdlskjflaksjfds'
        correct_out = []
        self.assertEqual(parse_emails(input_string), correct_out)

        input_string = 'one@a.com, two@gmail.com, three@uiuc.edu'
        correct_out = ['one@a.com', 'two@gmail.com', 'three@uiuc.edu']
        self.assertEqual(parse_emails(input_string), correct_out)

        input_string = 'one@a.com, asdf,,,,,,, two@gmail.com'
        correct_out = ['one@a.com', 'two@gmail.com']
        self.assertEqual(parse_emails(input_string), correct_out)

        input_string = 'one@a.c'
        correct_out = []
        self.assertEqual(parse_emails(input_string), correct_out)
