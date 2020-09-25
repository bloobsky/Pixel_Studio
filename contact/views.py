from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import ContactForm


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            # email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            fromwho = request.POST.get('fromwho', '')
            message = request.POST.get('message', '')
            try:
                send_mail(subject, message, fromwho, ['bloobsky@gmail.com'])
                print('sent')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'contact/success.html')
    return render(request, "contact/contact.html", {'form': form})
