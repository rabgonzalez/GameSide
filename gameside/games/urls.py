from django.urls import path

from . import views

urlpatterns = [
    path('/', views.game_list),
    path('<slug:game_slug>', views.game_detail),
    path('<slug:game_slug>/reviews', views.review_list),
    path('<slug:game_slug>/reviews/<int:review_id>', views.review_detail),
    path('<slug:game_slug>/reviews/add', views.add_review),
]
