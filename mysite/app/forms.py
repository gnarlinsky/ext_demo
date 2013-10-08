from django import forms
from localflavor.us.us_states import STATE_CHOICES
from app.models import EndUser
from app.helpers import parse_emails

class EndUserForm(forms.ModelForm):
    """ Creates a form based on the `EndUser` model.  """

    class Meta:
        """ Class container with various options (e.g. which fields should be
        rendered) attached to EndUserForm instance.
        """
        model = EndUser
        fields = ('first_name', 'last_name', 'street_address', 'city', 'state',
                  'phone', 'all_emails')
        widgets = {
            'all_emails': forms.Textarea(attrs={'cols': 60, 'rows': 4}),
        }

    def __init__(self, *arg, **kwarg):
        super(EndUserForm, self).__init__(*arg, **kwarg)
        # no empty forms
        self.empty_permitted = False

    def clean(self):
        """ Custom validation with custom error for text field with more than
        one email address.

        :returns: A dictionary of cleaned form fields
        """
        emails_field = self.cleaned_data.get('all_emails')
        if emails_field:
            valid_emails = parse_emails(emails_field)
            if not valid_emails:
                # attach custom error to this field
                self._errors['all_emails'] = self.error_class(
                    ['Please enter at least one valid email address']
                )
        return self.cleaned_data
