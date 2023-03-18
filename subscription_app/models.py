from calendar import month
from dataclasses import field
from pyexpat import model
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from datetime import timedelta


class Plan(models.Model):
    plan_choices = (
        ('basic', 'Basic'),
        ('silver', 'Silver'),
        ('gold', 'Gold'),

    )

    name = models.CharField(max_length=10, verbose_name="plan type", choices = plan_choices )
    price = models.FloatField()
    month = models.IntegerField(default=1)
    Active = models.BooleanField(default=True, verbose_name='Active status')

    def __str__(self):
        return f"{self.name} at {self.price}"

    @property
    def new_price(self):
        return self.price*100



class UserPlan(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=False)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(null=True)
    is_Active = models.BooleanField(default=False, verbose_name='Active')

    def __str__(self):
        return f"{self.user.username} on {self.plan.name}"

    @property
    def set_end_date(self):
        if self.is_Active == True:
            self.end_date = self.start_date + timedelta(days=30)
