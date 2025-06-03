from django.shortcuts import render
from .forms import ApplicationForm
from  .models import Form
from django.contrib import messages
from  django.core.mail import EmailMessage

def index (request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)

            messages_body = f"A new jop application was submitted. thank you{first_name}."
            email_message= EmailMessage("Form submission confirmation", messages_body, to=[email])
            email_message.send()

            messages.success(request,"form submitted")
    return render(request,"index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"New Contact Form Submission from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],  # Make sure this is defined in settings.py
            fail_silently=False,
        )

        messages.success(request, "Message sent successfully!")
        return redirect('contact')  # name of the contact URL in urls.py

    return render(request, 'contact.html')
