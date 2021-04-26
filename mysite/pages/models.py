from django.db import models

# Create your models here.

class Message(models.Model):
  sender = models.CharField(max_length=150) # Username lenght can be 150 in django user model?
  receiver = models.CharField(max_length=150)
  message_content = models.CharField(max_length=400)
  # pub_date = models.DateTimeField('date published')
