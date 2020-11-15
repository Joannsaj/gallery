from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns=[
    path('',views.index,name='home'),
    path('image/',views.display,name='image'),
    url(r'^image/(\d+)', views.get_image, name='photo'),
    path('search/', views.search_image, name='search_image'),
]
    # url(r'^image/(\d+)',views.article,name ='article')
