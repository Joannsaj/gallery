from django.db import models
from cloudinary.models import CloudinaryField

class Location(models.Model):
    location =  models.CharField(max_length =30)
    
    def __str__(self):
        return self.location

    def save_location(self):
        self.save

    def delete_location(self): 
        self.delete    

class Category(models.Model):    
    category =  models.CharField(max_length =30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save

    def delete_category(self): 
        self.delete

class Photo(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length =30)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete= models.SET_NULL, null= True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, default='')

    def __str__(self):
        return self.name     

    def save_image(self):
        self.save

    def delete_image(self): 
        self.delete

    @classmethod
    def images(cls):
        images = cls.objects.all()
        return images  

    @classmethod
    def update_image(cls, id): 
        images = cls.objects.filter(id=id).update(image = value)
        
    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.get(pk = id)

    @classmethod
    def search_image(cls, search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images

    @classmethod
    def filter_by_location(cls,location): 
       images = cls.objects.filter(location__location= location)