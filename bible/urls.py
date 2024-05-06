from django.urls import path
from bible import views

urlpatterns = [
    path('', views.home, name='home'),
]
