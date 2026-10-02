from django.shortcuts import render
from rest_framework.response import Response
from .serializers import BookingCreateSerializer
from rest_framework.views import APIView



class BookingCreateView(APIView):

    def post(self, request):

        serializer = BookingCreateSerializer(data=request.data)



