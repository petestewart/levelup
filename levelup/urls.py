from django.conf.urls import include
from django.urls import path
from levelupapi.views import register_user, login_user
from django.contrib import admin
urlpatterns = [
    path('register', register_user),
    path('admin/', admin.site.urls),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]

