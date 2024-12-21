from django.contrib import admin
from django.urls import path, include

from account.views import RegisterView, LoginView
from home.views import BlogView
 
urlpatterns = [
    path('account/', include('account.urls')),
    path('home/blog/', include('home.urls')),
]
