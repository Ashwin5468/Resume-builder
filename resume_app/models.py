from django.db import models

# Create your models here.

class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=100,default=" ")
    last_name = models.CharField(max_length=100,default=" ")
    email = models.EmailField(max_length=100,default=" ")
    phone_number = models.CharField(max_length=20,default=" ")
    address = models.CharField(max_length=200,default=" ")
    job_experience = models.TextField(max_length=200,default=" ")
    skills = models.TextField(max_length=200,default=" ")
    education = models.CharField(max_length=100, default=" ")
    # Add more fields as per your requirements