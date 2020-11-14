from django.shortcuts import render
from .models import Photo

# Create your views here.
def index(request):
    return render(request, 'index.html')

def display(request):
    image = Photo.images()
    return render(request,'pics.html',{"image": image})    

def get_image(request,image_id):
    try:
        image = Photo.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'image.html',{"image":image})    