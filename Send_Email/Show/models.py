from django.db import models

# Create your models here.
class Email_Content(models.Model):
    User_name = models.CharField(max_length=150)
    User_email = models.EmailField(max_length=250)
    User_subject = models.CharField(max_length=250)
    User_message = models.TextField()
    create_day = models.DateField(auto_now=True)
