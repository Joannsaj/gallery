from django.test import TestCase
from .models import Photo,Category,Location
# Create your tests here.

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.food= Category(category='Food')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.food,Category))    

    # Testing Save Method
    def test_save_method(self):
        self.food.save_category()
        cat = Category.objects.all()
        self.assertTrue(len(cat)>0)  

    # Testing delete Method
    def test_delete_method(self):
        self.food.delete_category()
        cat = Category.objects.all()
        self.assertTrue(len(cat)<1)        


class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.kampala= Location(location='Kampala')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kampala,Location))    

    # Testing Save Method
    def test_save_method(self):
        self.kampala.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0) 

    # Testing delete Method
    def test_delete_method(self):
        self.kampala.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) < 1)        


class PhotoTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Creating a new category and saving it
        self.food= Category(category='Food')
        self.food.save_category()

        # Creating a new location and saving it
        self.kampala= Location(location='Kampala')
        self.kampala.save_location()

        self.nature= Photo(location=self.kampala,category=self.food, name='nature',description='something something')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nature,Photo))    

    # Testing Save Method
    def test_save_method(self):
        self.nature.save_image()
        pictures = Photo.objects.all()
        self.assertTrue(len(pictures) > 0)  

    # Testing delete Method
    def test_delete_method(self):
        self.nature.delete_image()
        pictures = Photo.objects.all()
        self.assertTrue(len(pictures) < 1)        

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Photo.objects.all().delete()
