from django.urls import path

from . import views

urlpatterns = [
    path('/', views.game_list, name='game-list'),
    path('/<slug:game_slug>', views.game_detail, name='game-detail'),
]
