from django.urls import path
from .import views

urlpatterns = [
    path('data/',views.demo),
    path('course/access/', views.access),
]

