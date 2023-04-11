# collection/views.py
from rest_framework import generics
from user.models import User
from game.models import Game
from .models import Collection
from .serializers import CollectionSerializer, GameSerializer
from rest_framework.response import Response

class CollectionListCreateView(generics.ListCreateAPIView):
    queryset = Collection.objects.filter(delete_time__isnull=True)
    serializer_class = CollectionSerializer

class CollectionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.filter(delete_time__isnull=True)
    serializer_class = CollectionSerializer

class UserGameListView(generics.ListAPIView):
    serializer_class = GameSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Game.objects.filter(collection__user_id=user_id, collection__delete_time__isnull=True)

# class UserGamesView(generics.ListAPIView):
#     serializer_class = CollectionSerializer
#
#     def get_queryset(self):
#         user_id = self.kwargs['user_id']
#         return Collection.objects.filter(user_id=user_id)
#
#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         game_ids = queryset.values_list('game_id', flat=True)
#         games = Game.objects.filter(id__in=game_ids)
#         serializer = GameSerializer(games, many=True)
#         return Response(serializer.data)
