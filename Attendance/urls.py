from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r"^static/(?P<path>.*)$", serve, {'document_root': settings.STATIC_ROOT}),

    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view(), name='logout'),
    path('task/', include('task.urls')),
]
