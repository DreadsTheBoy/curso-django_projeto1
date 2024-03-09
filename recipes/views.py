'''
    Doc Modulo
'''

from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.


def home(request: HttpRequest):
    """
        Minha View Home
    """
    return render(request, 'recipes/home.html')
