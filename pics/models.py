from django.db import models
from cloudinary.models import CloudinaryField

class Photo(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length =30)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    def __str__(self):
        return self.name

    @classmethod
    def images(cls):
        images = cls.objects.all()
        return images

class Location(models.Model):
    location =  models.CharField(max_length =30)
    
    def __str__(self):
        return self.location

class Category(models.Model):    
    category =  models.CharField(max_length =30)

    def __str__(self):
        return self.category