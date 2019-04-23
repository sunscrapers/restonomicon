import django_filters
import pendulum
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


class BorrowedFilterSet(django_filters.FilterSet):
    missing = django_filters.BooleanFilter(field_name='returned', lookup_expr='isnull')
    overdue = django_filters.BooleanFilter(method='get_overdue', field_name='returned')

    class Meta:
        model = models.Borrowed
        fields = ['what', 'to_who', 'missing', 'overdue']

    def get_overdue(self, queryset, field_name, value, ):
        if value:
            return queryset.filter(when__lte=pendulum.now().subtract(months=2))
        return queryset


class BorrowedViewset(viewsets.ModelViewSet):
    queryset = models.Borrowed.objects.all()
    serializer_class = serializers.BorrowedSerializer
    permission_classes = [IsOwner]
    filterset_class = BorrowedFilterSet
