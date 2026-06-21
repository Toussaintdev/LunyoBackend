from django.urls import path
from .views import InscriptionView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('register/', InscriptionView.as_view()),
]
