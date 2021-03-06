import levelupreports
from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from levelupapi.views import register_user, login_user
from levelupapi.views import GameTypes, Games, Events

# from levelupreports import urls as reporturls

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypes, 'gametype')
router.register(r'games', Games, 'game')
router.register(r'events', Events, 'event')

from django.contrib import admin

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('admin/', admin.site.urls),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('levelupreports.urls')),
]
