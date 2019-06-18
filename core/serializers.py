from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Item


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'kind', 'rarity', 'avg_price', 'max_price', 'min_price')