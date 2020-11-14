from django.db import models
from cloudinary.models import CloudinaryField

class Location(models.Model):
    location =  models.CharField(max_length =30)
    
    def __str__(self):
        return self.location

class Category(models.Model):    
    category =  models.CharField(max_length =30)

    def __str__(self):
        return self.category

class Photo(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length =30)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete= models.SET_NULL, null= True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, default='')
    def __str__(self):
        return self.name

    @classmethod
    def images(cls):
        images = cls.objects.all()
        return images        