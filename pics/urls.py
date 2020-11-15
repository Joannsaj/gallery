from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='home'),
    path('image/',views.display,name='image'),
    path('image/<int:image_id>/', views.get_image, name='photo'),
    path('search/', views.search_image, name='search_image'),
]
