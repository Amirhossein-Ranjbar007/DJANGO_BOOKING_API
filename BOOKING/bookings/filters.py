import django_filters
from .models import Booking, BookingStatus
from listing.models import Space



class BookingFilter(django_filters.FilterSet):

    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    status = django_filters.ChoiceFilter(field_name='status', choices=BookingStatus.choices)
    space = django_filters.ModelChoiceFilter(field_name='space', queryset=Space.objects.all())
    start_after = django_filters.DateTimeFilter(field_name='start_at', lookup_expr='gte')
    start_before = django_filters.DateTimeFilter(field_name='start_at', lookup_expr='lte')

    class Meta:
        model = Booking
        fields = ['space', 'user', 'price', 'start_at', 'end_at', 'status']


