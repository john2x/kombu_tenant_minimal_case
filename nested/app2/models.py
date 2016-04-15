from django.db import models

class App2(models.Model):
    name = models.CharField(max_length=255)

