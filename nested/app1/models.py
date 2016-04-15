from django.db import models

class App1(models.Model):
    name = models.CharField(max_length=255)

