from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),          #GET request, renders index.html
    path('process', views.process),         #POST request
    path('result', views.result),           #GET request, renders result.html
    path('<url>', views.catch_all)          #This will catch any path not intended to have a page, if you include this it must be the LAST path listed      
]