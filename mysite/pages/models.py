from django.db import models

# Create your models here.

class Message(models.Model):
  sender = models.TextField()
  receiver = models.TextField()
  message_content = models.TextField()
  # pub_date = models.DateTimeField('date published')
