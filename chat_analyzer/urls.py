from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='chat_home'),
    path('analyze/', views.analyze_text, name='analyze_text'),
]
