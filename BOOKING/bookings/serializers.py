from rest_framework import serializers
from .models import Booking


class BookingCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ['space', 'start_at', 'end_at']

class BookingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ['space', 'price', 'status', 'start_at', 'end_at']


class BookingDetailListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ['space', 'user', 'status', 'price', 'start_at', 'end_at', 'created_at']





