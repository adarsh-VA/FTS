from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name = 'home'),
    path('bhome', views.bhome, name = 'bhome')
]