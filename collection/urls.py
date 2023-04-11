# collection/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('collection/', views.CollectionListCreateView.as_view(), name='collection-list-create'),
    path('collection/<int:pk>/', views.CollectionRetrieveUpdateDestroyView.as_view(), name='collection-retrieve-update-destroy'),
    path('user/<int:user_id>/games/', views.UserGameListView.as_view(), name='user-game-list'),
    # path('user/<int:user_id>/games/', views.UserGamesView.as_view(), name='user_games'),
]
