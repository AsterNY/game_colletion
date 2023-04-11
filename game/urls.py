from django.urls import path
from . import views

urlpatterns = [
    path('games/', views.GameListCreateView.as_view(), name='game_list_create'),
    path('games/<int:pk>/', views.GameRetrieveUpdateDestroyView.as_view(), name='game_retrieve_update_destroy'),
]
