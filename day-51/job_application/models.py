from django.db import models

class Form(models.Model):
    first_Name = models.CharField(max_length=80)
    last_Name = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)
    date = models.DateField()
    occupation = models.CharField(max_length=80)





