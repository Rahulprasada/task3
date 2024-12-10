from django.urls import path # type: ignore
from . import views  # Import views from your app

urlpatterns = [
    path('', views.login, name='home'),  # Maps the root URL to the 'home' view
    path('about/', views.signup, name='about'),  # Maps '/about' to the 'about' view
]
