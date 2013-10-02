from django.test import TestCase
from app.models import EndUser
from app.forms import EndUserForm
from ttools import t_info

# TODO: more comprehensive test cases for incorrect field inputs

class FormsTests(TestCase):
    def setUp(self):
        t_info("TestCase FormsTests", 1)
        t_info(self._testMethodName + ": " + self._testMethodDoc, 3)

    # TODO: create functional parallel for this test (hitting 'submit'
    # without filling any fields should not work)
    def test_no_empty_permitted(self):
        """
        Test that empty_permitted is set to False upon creation (i.e. cannot
        submit an empty form).
        """
        eu_form = EndUserForm()
        self.assertEqual(eu_form.empty_permitted, False)

    def test_cant_submit_empty_form(self):
        """
        Test that an empty form does not validate.
        """
        form_data = {}  # empty
        eu_form = EndUserForm(data=form_data)
        self.assertEqual(eu_form.is_valid(), False)

    def test_empty_form_errors(self):
        """
        Test that submitting empty form returns 'this field required' errors
        for every field.
        """
        form_data = {}
        eu_form = EndUserForm(data=form_data)
        eu_form.is_valid()  # attempt to validate to get errors
        correct_errors = {'all_emails': [u'This field is required.'],
                          'city': [u'This field is required.'],
                          'first_name': [u'This field is required.'],
                          'last_name': [u'This field is required.'],
                          'phone': [u'This field is required.'],
                          'state': [u'This field is required.'],
                          'street_address': [u'This field is required.']}
        self.assertEqual(eu_form._errors, correct_errors)

    def test_can_submit_correct_form(self):
        """
        Test that correct form validates.
        """
        form_data = {'all_emails': 'test@uiuc.edu',
                     'city': 'Chicago',
                     'first_name': 'Jane',
                     'last_name': 'Doe',
                     'phone': '1234567890',
                     'state': 'IL',
                     'street_address': '1 North St.'}
        eu_form = EndUserForm(data=form_data)

        self.assertEqual(eu_form.is_valid(), True)

    def test_no_form_errors(self):
        """
        Test that submitting a form with all fields correctly filled does not
        return any errors.
        """
        form_data = {'all_emails': 'test@uiuc.edu',
                     'city': 'Chicago',
                     'first_name': 'Jane',
                     'last_name': 'Doe',
                     'phone': '1234567890',
                     'state': 'IL',
                     'street_address': '1 North St.'}
        eu_form = EndUserForm(data=form_data)
        eu_form.is_valid()  # attempt to validate to get errors
        correct_errors = {}
        self.assertEqual(eu_form._errors, correct_errors)

    def test_clean(self):
        """ Test that if the Emails ('all_emails') field does not contain at
        least one valid email address, the correct error is returned.
        """
        form_data = {'all_emails': 'asldjflsdkjf',
                     'city': 'Chicago',
                     'first_name': 'Jane',
                     'last_name': 'Doe',
                     'phone': '1234567890',
                     'state': 'IL',
                     'street_address': '1 North St.'}
        eu_form = EndUserForm(data=form_data)
        eu_form.is_valid()  # attempt to validate to get errors
        corr_error = eu_form.error_class(
            ['Please enter at least one valid email address']
        )
        self.assertEqual(eu_form._errors['all_emails'], corr_error)

