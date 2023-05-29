from django.urls import path
from .import views

app_name = 'prizedraw'
#http://localhost:8000/partners/create/
urlpatterns = [

    path('create/prizedraw/', views.CreatePrizeDraw, name="create_prize_draw"),
]