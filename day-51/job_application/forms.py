from django import forms

class ApplicationForm(forms.Form):
    first_Name = forms.CharField(max_length=80)
    last_Name = forms.CharField(max_length=80)
    email = forms.EmailField(max_length=80)
    date = forms.DateField()
    occupation = forms.CharField(max_length=80)

