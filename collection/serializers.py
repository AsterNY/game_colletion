# collection/serializers.py
from rest_framework import serializers
from user.models import User
from game.models import Game
from .models import Collection

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class CollectionSerializer(serializers.ModelSerializer):
    game = GameSerializer()

    class Meta:
        model = Collection
        fields = '__all__'
