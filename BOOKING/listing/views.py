from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter, SearchFilter
from .serializers import CategorySerializer
from .models import Category
from .pagination import CategoryPagination



class CategoryView(ListAPIView):

    categories = Category.objects.all()
    serializer = CategorySerializer

    pagination_class = CategoryPagination
    filter_backends = [SearchFilter]

    search_fields = ['name', 'slug']











