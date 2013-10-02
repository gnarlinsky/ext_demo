from django.test import TestCase
from app.admin import EmailFormSet
from app.models import EndUser
from app.forms import EndUserForm
from ttools import t_info

# TODO: more comprehensive test cases; parallel functional tests
class AdminTests(TestCase):
    def setUp(self):
        t_info("TestCase AdminTests", 1)
        t_info(self._testMethodName + ": " + self._testMethodDoc, 3)

    def test_clean(self):
        """
        Test custom validation -- if admin attempting to delete all email
        addresses for current enduser, does the correct validation error get
        raised?
        """
#        efs = EmailFormSet()
#        efs.is_valid()
#        # create enduser and several emails
#        enduser = EndUser.objects.create(first_name='Lisa', last_name='Simpson')
#        EndUserEmail.objects.create(email='test1@email.com', enduser=enduser)
#        EndUserEmail.objects.create(email='test2@email.com', enduser=enduser)
#        EndUserEmail.objects.create(email='test3@email.com', enduser=enduser)
#        self.assertEqual(enduser.emails(),
#                          'test1@email.com, test2@email.com, test3@email.com')
