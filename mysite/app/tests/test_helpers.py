from django.test import TestCase
from app.helpers import parse_emails
from ttools import t_info

class HelpersTests(TestCase):
    def setUp(self):
        t_info('TestCase HelpersTests', 1)
        t_info(self._testMethodName + ': ' + self._testMethodDoc, 3)

    def test_helpers(self):
        """
        Test that valid email addresses are parsed from string.
        """
        t_info('Is empty string parsed correctly?', 5)
        input_string = ''
        correct_out = []
        self.assertEqual(parse_emails(input_string), correct_out)

        t_info('Is a single non-email string parsed correctly?', 5)
        input_string = 'alskjfdlskjflaksjfds'
        correct_out = []
        self.assertEqual(parse_emails(input_string), correct_out)

        t_info('Are multiple emails, separated by punctuation, parsed correctly?', 5)
        input_string = 'one@a.com, two@gmail.com, three@uiuc.edu'
        correct_out = ['one@a.com', 'two@gmail.com', 'three@uiuc.edu']
        self.assertEqual(parse_emails(input_string), correct_out)

        t_info('Is a string with valid as well as invalid emails parsed correctly?', 5) 
        input_string = 'one@a.com, asdf,,,,,,, two@gmail.com'
        correct_out = ['one@a.com', 'two@gmail.com']
        self.assertEqual(parse_emails(input_string), correct_out)

        t_info('Is a string with one invalid email parsed correctly?', 5)
        input_string = 'one@a.c'
        correct_out = []
        self.assertEqual(parse_emails(input_string), correct_out)
