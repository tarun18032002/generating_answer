from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_docx, name='upload'),
    path('generate/', views.generate_answers, name='generate'),
]