from django.db import models
# Create your models here.

class upload(models.Model):
    id1 = models.IntegerField()
    name = models.CharField(max_length=255)
    #img: str
    price = models.IntegerField()
    count = models.IntegerField()
    class Meta:
        app_label = 'upload'

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    class Meta:
        app_label = 'person'
    