from django.db import models

class createmodel(models.Model):
    studentnumber=models.IntegerField()
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    mobile=models.IntegerField()
    email=models.EmailField(max_length=50)



