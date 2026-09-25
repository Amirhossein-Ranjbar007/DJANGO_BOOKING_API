from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter, SearchFilter
from .serializers import CategorySerializer,SpaceSerializer
from .models import Category, Space
from .pagination import CategoryPagination, SpacePagination
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from .filters import SpaceFilter



class CategoryView(ListAPIView):

    categories = Category.objects.all()
    serializer_class = CategorySerializer

    pagination_class = CategoryPagination
    filter_backends = [SearchFilter]

    search_fields = ['name', 'slug']



class SpaceListView(ListAPIView):

    queryset = Space.objects.all()
    serializer_class = SpaceSerializer

    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]

    ordering_fields = ['city', 'created_at', 'title', 'price']
    ordering = ['-created_at']

    pagination_class = SpacePagination
    search_fields = ['title', 'city', 'host__name']
    filterset_class = SpaceFilter













