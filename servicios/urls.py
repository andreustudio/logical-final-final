from django.urls import path
from . import views

app_name = 'servicios'

urlpatterns = [
    path('servicios/', views.servicios, name='servicios'),
    path('<slug:slug>/', views.ServicioDetailView.as_view(), name='servicio_detail'),
]