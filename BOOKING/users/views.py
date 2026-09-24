from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (UserRegisterSerializer,UserSerializer,ChangePasswordSerializer,
UserLogoutSerializer)

from .models import User
from .throttlers import RegisterThrottle,ProfileThrottle,ChangePasswordThrottle
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from rest_framework import status


class UserRegisterView(APIView):
    throttle_classes = [RegisterThrottle]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [ProfileThrottle]

    def get(self, request):
        serializer = UserSerializer(instance=request.user)
        return Response(serializer.data)

class UserChangeProfileView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def patch(self, request):
        serializer = UserSerializer(instance=request.user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [ChangePasswordThrottle]

    def patch(self, request):
        serializer = ChangePasswordSerializer(instance=request.user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = UserLogoutSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=204)



