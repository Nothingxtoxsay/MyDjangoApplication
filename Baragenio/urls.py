from django.urls import path
from .views import HomePageView, AboutPageView, login_view, register_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]
