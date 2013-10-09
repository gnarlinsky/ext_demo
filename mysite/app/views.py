from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from app.models import EndUser, EndUserEmail
from app.forms import EndUserForm
from app.helpers import parse_emails


def signup_admin(request):
    """ Redirect to EndUser administration
    """
    return HttpResponseRedirect('/admin/app/enduser')

def signup(request):
    """ Display and process sign up form.
    """

    if request.method == 'POST':   # if form is being submitted
        eu_form = EndUserForm(request.POST)
        if eu_form.is_valid():
            eu_form.save()
            # Parse out the email addresses from text field input, and save
            # them as EndUserEmail instances, each with a FK to its EndUser.
            emails_string = eu_form.cleaned_data['all_emails']
            emails = parse_emails(emails_string)
            enduser = EndUser.objects.latest('id')
            # save each email as an EndUserEmail instance
            for email in emails:
                email = EndUserEmail(email=email, enduser=enduser)
                email.save()
            messages.success(request, 'submit_success')
            # clear form
            eu_form = EndUserForm()
            return HttpResponseRedirect(request.path)
    else:  # viewing form, not submitting
        eu_form = EndUserForm()
    return render_to_response('signup.html',
                              {'eu_form': eu_form },
                              context_instance=RequestContext(request)
                             )
