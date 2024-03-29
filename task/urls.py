from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='task'),
    path('create', views.create, name='task_create'),
    path('join', views.join, name='task_join'),
    path('detail/<int:id>', views.detail, name='task_detail'),
    path('delete/<int:task_id>', views.delete, name='task_delete'),
    path('enroll/<int:task_id>', views.check, name='task_enroll'),

    path('export/<task_id>', views.export_task_xls, name='export_task_xls'),
]