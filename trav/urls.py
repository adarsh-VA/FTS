from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name = 'home'), 
    path('upload', views.upload, name = 'upload'),
    path('bhome', views.bhome, name = 'bhome'),
    path('receive', views.receive, name = 'receive')
]