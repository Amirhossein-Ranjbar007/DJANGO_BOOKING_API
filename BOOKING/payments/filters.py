import django_filters

from .models import Payments


class PaymentListFilter(django_filters.FilterSet):

    min_amount = django_filters.NumberFilter(field_name='amount', lookup_expr='gte')
    max_amount = django_filters.NumberFilter(field_name='amount', lookup_expr='lte')

    before = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    after = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Payments
        fields = ['min_amount', 'max_amount', 'before', 'after']

