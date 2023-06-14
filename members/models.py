from django.db import models
from plans.models import Plan

class Member(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default=1) 
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=17, null=True)
    joined_date = models.DateTimeField(null=True) 

    def __str__(self):
        return f"{self.firstname} {self.lastname}"