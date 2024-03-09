'''
    Doc Modulo
'''
from django.urls import path

from recipes.views import contato, home, sobre

# HTTP request


urlpatterns = [
    path('', home),  # Home
    path('sobre/', sobre),  # /sobre/
    path('contato/', contato),  # /contato
]
