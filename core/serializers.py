from rest_framework import serializers
from . import models


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Friend
        fields = ('id', 'name')


class BelongingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Belonging
        fields = ('id', 'name')


class BorrowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Borrowed
        fields = ('id', 'what', 'to_who', 'when', 'returned')
