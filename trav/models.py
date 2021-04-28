from django.db import models

# Create your models here.
class destination(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)

class f(models.Model):
    ff = models.FileField()

class userinfo(models.Model):
    uniqueid = models.TextField()
    foldername = models.TextField()
    filedic = models.TextField()
