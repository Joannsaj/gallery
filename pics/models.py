from django.db import models
from cloudinary.models import CloudinaryField

class Photo(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length =30)
    description = models.TextField()
    # location
    # category
    def __str__(self):
        return self.title

    @classmethod
    def images(cls):
        images = cls.objects.all()
        return images

class Location(models.Model):
    country =  models.CharField(max_length =30)
    street =  models.CharField(max_length =30)

class Category(models.Model):    
    category =  models.CharField(max_length =30)