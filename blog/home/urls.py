from django.contrib import admin
from django.urls import path

from home.views import BlogView
 
urlpatterns = [
    path('', BlogView.as_view()), 

]
