from django.db import models
from localflavor.us.us_states import STATE_CHOICES

class EndUser(models.Model):
    """ docstring go here """
    first_name = models.CharField(max_length=25, blank=False, null=False)
    last_name = models.CharField(max_length=25, blank=False, null=False)
    street_address = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=2, blank=False, null=False,
                             choices=STATE_CHOICES)
    city = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    all_emails = models.TextField('Email(s)', blank=False, null=False)

    def emails(self):
        """ Return all email addresses associated with this enduser """
        # referring to the "reverse" of a ForeignKey (many-to-one) relationship
        all_emails = [e.__unicode__() for e in self.enduseremail_set.all()]
        return ', '.join(all_emails)

    def __unicode__(self):
        """ Represent this object with first name and last name """
        return '{} {}'.format(self.first_name, self.last_name)

class EndUserEmail(models.Model):
    """ docstring placeholder """
    enduser = models.ForeignKey(EndUser)
    email = models.EmailField(max_length=100, blank=False, null=False)

    def __unicode__(self):
        """ Represent object with email address """
        return self.email
