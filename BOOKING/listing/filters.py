import django_filters
from .models import Space



class SpaceFilter(django_filters.FilterSet):

    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')

    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    min_capacity = django_filters.NumberFilter(field_name='capacity', lookup_expr='gte')

    max_capacity = django_filters.NumberFilter(field_name='capacity',lookup_expr='lte')

    class Meta:
        model = Space
        fields = ['category', 'host', 'city', 'min_price', 'max_price', 'min_capacity', 'max_capacity']














