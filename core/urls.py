from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('servicios/', views.servicios, name='servicios'),  # Servicios page
]