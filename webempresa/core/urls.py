from django.urls import path
from . import views as core_views
from django_distill import distill_path

# Función para distill_path en home
def get_index():
    return None  # No hay parámetros dinámicos

# Función para distill_path en about
def get_about():
    return None  # No hay parámetros dinámicos

# Función para distill_path en store
def get_store():
    return None  # No hay parámetros dinámicos

urlpatterns = [
    distill_path('', core_views.home, name='home', distill_func=get_index),
    distill_path('about/', core_views.about, name='about', distill_func=get_about),
    distill_path('store/', core_views.store, name='store', distill_func=get_store),
]
