from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='task'),
    path('create', views.create, name='task_create'),
    path('join', views.join, name='task_join'),
    path('detail/<int:id>', views.detail, name='task_detail'),
    path('enroll/<int:task_id>', views.check, name='task_enroll'),
]