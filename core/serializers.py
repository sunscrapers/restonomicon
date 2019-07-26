from dynamic_rest.fields import DynamicRelationField
from dynamic_rest.serializers import DynamicModelSerializer
from rest_framework import serializers

from . import models


class FriendSerializer(DynamicModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Friend
        fields = ("id", "name", "owner", "has_overdue")
        deferred_fields = ("has_overdue",)


class BelongingSerializer(DynamicModelSerializer):
    class Meta:
        model = models.Belonging
        fields = ("id", "name")


class BorrowedSerializer(DynamicModelSerializer):
    what = DynamicRelationField("BelongingSerializer")
    to_who = DynamicRelationField("FriendSerializer")

    class Meta:
        model = models.Borrowed
        fields = ("id", "what", "to_who", "when", "returned")
