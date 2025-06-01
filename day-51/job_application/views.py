from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)  # required for form validation
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            print(first_name)

            Form.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date=date,
                occupation=occupation
            )

            messages.success(request, "Form submitted")
        else:
            messages.error(request, "Invalid form data.")
    return render(request, "index.html")
