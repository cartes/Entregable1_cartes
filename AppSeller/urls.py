from django.urls import path
from AppSeller import views

urlpatterns = [
    path('', views.inicio)
]