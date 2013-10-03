from django import forms
from localflavor.us.us_states import STATE_CHOICES
from app.models import EndUser
from app.helpers import parse_emails

class EndUserForm(forms.ModelForm):
    """ docstring placeholder """
    class Meta:
        """ docstring placeholder """
        model = EndUser
        # TODO: so the below was complaining that it could not find the
        # 'emails' field, so I just commented it out (i need all of them
        # anyway)... but what if it's a
        # symptopm of a bigger problem?
        fields = ('first_name', 'last_name', 'street_address', 'city', 'state',
                  'phone', 'all_emails')
        widgets = {
            'all_emails': forms.Textarea(attrs={'cols': 60, 'rows': 4}),
        }

    def __init__(self, *arg, **kwarg):
        super(EndUserForm, self).__init__(*arg, **kwarg)
        self.empty_permitted = False

    def clean(self):
        """ Custom validation for text field with more than one email address.
        """
        # TODO: what happens if field is empty on submit? 
        emails_field = self.cleaned_data.get('all_emails')
        if emails_field:
            valid_emails = parse_emails(emails_field)
            if not valid_emails:
                # attach custom error to this field
                self._errors['all_emails'] = self.error_class(
                    ['Please enter at least one valid email address']
                )
        return self.cleaned_data
