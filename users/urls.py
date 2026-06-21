from django.urls import path
from .views import InscriptionView, ProfilCurrentView, ProfilView, UserListView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', InscriptionView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('profil/me/', ProfilCurrentView.as_view()),
    path('profil/<str:username>/', ProfilView.as_view()),
    path('', UserListView.as_view()),
    path('<uuid:pk>/', UserDetailView.as_view()),
]
