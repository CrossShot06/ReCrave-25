from django.urls import path
from . import views  # Imports views from the current app

urlpatterns = [

    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('register/success/', views.register_success, name='register_success'),
]