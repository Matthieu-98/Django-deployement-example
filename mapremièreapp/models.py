from django.db import models

class Member(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    pwd = models.CharField(max_length=100)
    age = models.IntegerField(max_length=3)
    
    def __str__(self):
        return self.fname + ' ' + self.lname