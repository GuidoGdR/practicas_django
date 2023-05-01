from django.db import models

# Create your models here.

class project(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField(max_length=20000)

    technology = models.CharField(max_length=200)

    created_date = models.DateTimeField(auto_now_add=True)
