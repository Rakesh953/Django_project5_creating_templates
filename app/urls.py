from django.urls import path
from app.views import *
app_name='hey'

urlpatterns=[
    path('temp/',temp,name='temp'),
]