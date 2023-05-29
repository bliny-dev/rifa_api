from django.urls import path, include
from .import views
app_name = 'accounts'

urlpatterns = [
    path('register/', views.Register, name='register'),
    path('login/', views.Login, name='accounts'),
    
]
