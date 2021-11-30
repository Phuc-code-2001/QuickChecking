from django.urls import path
from .views import index, login

urlpatterns = [
    path('', index, name='home'),
    path('login/', login, name='login')
]