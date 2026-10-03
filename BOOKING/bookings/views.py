from django.shortcuts import render
from rest_framework.response import Response
from .serializers import BookingCreateSerializer,BookingListSerializer, BookingDetailListSerializers
from rest_framework.views import APIView
from .services import create_booking
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .throttling import BookingCreateThrottle
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .models import Booking
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookingFilter
from .pagination import BookingPagination
from django.core.cache import cache
from django.shortcuts import get_object_or_404
import time



class BookingCreateView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [BookingCreateThrottle]


    def post(self, request):

        serializer = BookingCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        book = serializer.validated_data
        create_booking(user=request.user, space=book.space, start_at=book.start_at, end_at=book.end_at)

        return Response(status=status.HTTP_201_CREATED)


class BookingListView(ListAPIView):

    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    serializer_class = BookingListSerializer

    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]

    search_fields = ['space__name']

    ordering_fields = ['price', 'status', 'start_at']
    ordering = ['status']

    filterset_class = BookingFilter

    pagination_class = BookingPagination

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        user_id = request.user.id
        query_params =request.query_params.urlencode()
        ts_key = f"booking_ts_{user_id}"
        timestamp = cache.get_or_set(ts_key, time.time)
        cache_key = f"booking_list_{user_id}_{timestamp}_{query_params}"

        cached_data = cache.get(cache_key)
        if cached_data is not None:
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)
        cache.set(cache_key,response.data, timeout=120)
        return response

class BookingDetailListView(APIView):

    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get(self, request, id):

        cache_key = f"BookingDetail:{id}"
        cached_data = cache.get(cache_key)

        if cached_data is not None:
            return Response(cached_data)

        queryset = get_object_or_404(Booking, pk=id)
        serializer = BookingDetailListSerializers(instance=queryset, many=True)
        cache.set(cache_key, serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)















