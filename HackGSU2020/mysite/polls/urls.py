#mysite/urls.py
from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', include('pages.urls')), # new
    path('', views.index, name='index'),
]
