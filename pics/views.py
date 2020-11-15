from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
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

def search_image(request):  
    if 'picture' in request.GET and request.GET["picture"]:
        search_term = request.GET.get("picture")
        pictures = Photo.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"pictures": pictures})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})