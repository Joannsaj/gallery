from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='home'),
    path('image/',views.display,name='image'),
]