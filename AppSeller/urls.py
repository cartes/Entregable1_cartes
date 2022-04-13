from django.urls import path
from AppSeller import views

urlpatterns = [
    path('', views.inicio),
    path('publicar/', views.publicar),
    path('buscar/', views.buscar, name="Buscar"),
]