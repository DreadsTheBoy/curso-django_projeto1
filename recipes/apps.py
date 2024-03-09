'''
    DocString
'''
from django.apps import AppConfig


class RecipesConfig(AppConfig):
    """Classe que representa uma configuração de aplicativo"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipes'
