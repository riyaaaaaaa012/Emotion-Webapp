from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='image_home'),
    path('', views.detect_emotion, name='detect_emotion'),
    # path('', views.analyze_image, name='analyze_image'),
]
