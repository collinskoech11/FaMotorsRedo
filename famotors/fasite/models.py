from django.db import models

# Create your models here.
class ContactForm(models.Model):
    brand = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=200)