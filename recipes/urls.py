'''
    Doc Modulo
'''
from django.urls import path

from recipes.views import home

# HTTP request


urlpatterns = [
    path('', home),  # Home
]
