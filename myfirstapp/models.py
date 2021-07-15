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

class addcart(models.Model):
    id2 = models.IntegerField()
    name2 = models.CharField(max_length=255)
    images2 = models.ImageField(upload_to='media/')
    price2 = models.IntegerField()
    count2 = models.IntegerField()
    class Meta:
        app_label = 'addcart'
    