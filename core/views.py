from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def home(request):
    context = {'home': 'active'}
    return render(request, 'core/home.html', context)


def contact(request):
    context = {'contact': 'active'}
    if request.method == 'POST':
        input_name = request.POST['inputName']
        input_email = request.POST['inputEmail']
        input_subject = request.POST['inputSubject']
        input_message = request.POST['inputTextarea']

        # send email
        send_mail(
            input_subject,  # subject
            input_message,  # message
            input_email,  # from email
            ['jein9454@gmail.com'],  # To Email

        )

        return render(request, "core/contact.html", {"message_name": input_name})

    return render(request, "core/contact.html", context)
