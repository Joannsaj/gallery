from django.shortcuts import render
from .models import Photo

# Create your views here.
def index(request):
    return render(request, 'index.html')

def display(request):
    image = Photo.images()
    return render(request,'pics.html',{"image": image})    