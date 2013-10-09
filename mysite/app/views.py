from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from app.models import Customer, CustomerEmail
from app.forms import CustomerForm
from app.helpers import parse_emails


def signup_admin(request):
    """ Redirect to Customer administration
    """
    return HttpResponseRedirect('/admin/app/customer')

def signup(request):
    """ Display and process sign up form.
    """

    if request.method == 'POST':   # if form is being submitted
        eu_form = CustomerForm(request.POST)
        if eu_form.is_valid():
            eu_form.save()
            # Parse out the email addresses from text field input, and save
            # them as CustomerEmail instances, each with a FK to its Customer.
            emails_string = eu_form.cleaned_data['all_emails']
            emails = parse_emails(emails_string)
            customer = Customer.objects.latest('id')
            # save each email as an CustomerEmail instance
            for email in emails:
                email = CustomerEmail(email=email, customer=customer)
                email.save()
            messages.success(request, 'submit_success')
            # clear form
            eu_form = CustomerForm()
            return HttpResponseRedirect(request.path)
    else:  # viewing form, not submitting
        eu_form = CustomerForm()
    return render_to_response('signup.html',
                              {'eu_form': eu_form },
                              context_instance=RequestContext(request)
                             )
