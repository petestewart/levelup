from django.urls import path
from .views import usergame_list, gamerevent_list

urlpatterns = [
    path('reports/usergames', usergame_list),
    path('reports/userevents', gamerevent_list),
]
