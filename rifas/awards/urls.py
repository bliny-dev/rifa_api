from django.urls import path
from .import views

app_name = 'awards'
#http://localhost:8000/partners/create/
urlpatterns = [

    path('create/awards/<str:pk>/', views.CreateAwards, name="create_awards"),
]