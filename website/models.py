from statistics import mode
from django.db import models

# Create your models here.
class Hyperlink(models.Model):
    registration_google_form = models.TextField()
    group_invite_link = models.TextField()