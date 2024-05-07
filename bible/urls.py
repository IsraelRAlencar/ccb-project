from django.urls import path
from bible import views

app_name = 'bible'

urlpatterns = [
    path('', views.home_view, name='home'),
]
