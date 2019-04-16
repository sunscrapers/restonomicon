from rest_framework import viewsets

from . import models
from . import serializers
from .permissions import IsOwner


class FriendViewset(viewsets.ModelViewSet):
    queryset = models.Friend.objects.with_overdue()
    serializer_class = serializers.FriendSerializer
    permission_classes = [IsOwner]


class BelongingViewset(viewsets.ModelViewSet):
    queryset = models.Belonging.objects.all()
    serializer_class = serializers.BelongingSerializer
    permission_classes = [IsOwner]


class BorrowedViewset(viewsets.ModelViewSet):
    queryset = models.Borrowed.objects.all()
    serializer_class = serializers.BorrowedSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        qs = super().get_queryset()
        only_missing = str(self.request.query_params.get('missing')).lower()
        if only_missing in ['true', '1']:
            return qs.filter(returned__isnull=True)
        return qs
