from django.db import models
from localflavor.us.us_states import STATE_CHOICES
from django.db.models import signals
from django.contrib.auth.management import create_superuser
from django.contrib.auth import models as auth_models
from django.conf import settings

class EndUser(models.Model):
    """ Model representing user's contact information.
    """

    first_name = models.CharField(max_length=25, blank=False, null=False)
    last_name = models.CharField(max_length=25, blank=False, null=False)
    street_address = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=2, blank=False, null=False,
                             choices=STATE_CHOICES)
    city = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    all_emails = models.TextField('Email(s)', blank=False, null=False)

    def emails(self):
        """ Gather all email addresses associated with this enduser.

        :returns: A string of email addresses, separated by commas
        """
        # referring to the "reverse" of a ForeignKey (many-to-one) relationship
        all_emails = [e.__unicode__() for e in self.enduseremail_set.all()]
        return ', '.join(all_emails)

    def __unicode__(self):
        """ Represent this object with first name and last name.
        """
        return '{} {}'.format(self.first_name, self.last_name)

class EndUserEmail(models.Model):
    """ Model representing email address, with ForeignKey (i.e. many-to-one
    relationship) to an EndUser.
    """
    enduser = models.ForeignKey(EndUser)
    email = models.EmailField(max_length=100, blank=False, null=False)

    def __unicode__(self):
        """ Represent object with email address.
        """
        return self.email


####################################################################
# Prevent interactive question about wanting a superuser created.
####################################################################
# From http://stackoverflow.com/questions/1466827/ --
# Prevent interactive question about wanting a superuser created.  (This code
# has to go in the "models" module so that it gets processed by the "syncdb"
# command during database creation.)
# pragma: no cover  (exclude this code from coverage)
signals.post_syncdb.disconnect(
    create_superuser, sender=auth_models,
    dispatch_uid='django.contrib.auth.management.create_superuser')


# Create our own test user automatically.
def create_testuser(app, created_models, verbosity, **kwargs):  # pragma: no cover
    if not settings.DEBUG:
        return
    try:
        auth_models.User.objects.get(username='homer')
    except auth_models.User.DoesNotExist:
        print '*' * 80
        print 'Creating test user -- login: homer, password: homer'
        print '*' * 80
        assert auth_models.User.objects.create_superuser(
            'homer', 'homer@gmail.com', 'homer')
    else:
        print 'User homer (password homer) already exists'

signals.post_syncdb.connect(
    create_testuser, sender=auth_models,
    dispatch_uid='common.models.create_testuser')
