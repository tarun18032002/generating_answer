# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('upload/', views.upload_questions, name='upload'),
#     path('generate/', views.generate_answers, name='generate'),
# ]


### urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_questions, name='home'),
    path('batch/<uuid:batch_id>/', views.view_batch, name='view_batch'),
]