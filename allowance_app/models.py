from django.db import models
from datetime import date

from django.urls import reverse

# Create your models here.

# Create your models here.
#models are the Database tables 

#blank - if required or not. If False, must be true
#null = must be filled out in the form

class Allowance_app(models.Model):
    category = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(blank = True, decimal_places=2, max_digits=10000, null=True)
    date = models.DateField(default=date.today)
    allowance_no_debt_spending = models.IntegerField(default = 25, blank=True, null=True)
    credit = models.BooleanField(blank=True, null=False)

class Allowance_input_app(models.Model):
    allowance_no_debt = models.IntegerField(default = 45, blank=True, null=True)
    date = models.DateField(default=date.today)

