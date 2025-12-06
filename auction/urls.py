from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clubs/', views.clubs, name='clubs'),
    path('clubs/<int:team_id>/', views.team_detail, name='team_detail'),
    path('players/', views.players, name='players'),
    path('auction/<int:player_id>/', views.auction, name='auction'),
    path('assigned/<int:player_id>/<int:team_id>/', views.assigned, name='assigned'),
]
