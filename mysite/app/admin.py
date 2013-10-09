from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from app.models import EndUser, EndUserEmail
from django.core.exceptions import ValidationError



class EmailFormSet(BaseInlineFormSet):
    """ Custom validation. """

    def clean(self):
        """ Custom validation to ensure EndUser not left without any emails.

        :raises: ValidationError
        :returns: A dictionary or list of dictionaries of cleaned form fields
        """
        # Is the admin trying to delete every email for this enduser? (I.e. is
        # every non-empty dict's DELETE set to True?) If so, create error.
        try:
            all_emails = [eu_email for eu_email in self.cleaned_data if eu_email]
            emails_to_del = [eu_email for eu_email in all_emails if eu_email.get('DELETE')]
            num_emails_to_del = len(emails_to_del)
            num_all_emails = len(all_emails)
            if num_all_emails == num_emails_to_del:
                raise ValidationError('At least one email address is required')
        except:
            raise ValidationError('At least one email address is required')
        return self.cleaned_data


class EmailInline(admin.TabularInline):
    """ Options for inline editing of EndUserEmail instances
    """
    model = EndUserEmail
    formset = EmailFormSet
    extra = 2 # by default, provide two email fields


class EndUserAdmin(admin.ModelAdmin):
    """ Define options and customization for admin. """

    # add ability to edit emails directly on the end user page/form
    inlines = [EmailInline]

    ###########################################################################
    # what to display on change_list (columns, filter, ... )
    ###########################################################################
    list_display = ('first_name', 'last_name', 'street_address', 'city', 'state',
                    'phone', 'emails')
    list_display_links = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name',
                     'street_address', 'city', 'state',
                     'all_emails', 'phone']

    ###########################################################################
    # what to show, in what order, on change_form
    ###########################################################################
    fieldsets = [
        (None, {'fields': ['first_name', 'last_name']}),
        (None, {'fields': ['street_address', 'city', 'state', 'phone']}),
    ]

    def has_add_permission(self, request, obj=None):
        """ Remove admin's ability to add more EndUser objects; don't display
        'Save and Add' button on change_form and 'Add New' button on
        change_list.
        """
        return False

admin.site.register(EndUser, EndUserAdmin)
