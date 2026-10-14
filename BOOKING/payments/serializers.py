from rest_framework import serializers
from .models import Payments, PaymentTransaction
from bookings.models import Booking


class PaymentCreateSerializer(serializers.Serializer):

    booking = serializers.PrimaryKeyRelatedField(queryset=Booking.objects.all())



class PaymentListSerializer(serializers.ModelSerializer):

    space_name = serializers.CharField(source='booking.space.title', read_only=True)

    class Meta:
        model = Payments
        fields = ['space_name', 'status', 'amount', 'created_at']

