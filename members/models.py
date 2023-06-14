from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=17, null=True)
    joined_date = models.DateTimeField(null=True) 

    def __str__(self):
        return f"{self.firstname} {self.lastname}"