from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer,UserSerializer
from .models import User
from .throttlers import RegisterThrottle


class UserRegisterView(APIView):
    throttle_classes = [RegisterThrottle]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        vd = serializer.validated_data
        user = User(email=vd['email'], first_name=vd['first_name'], last_name=vd['last_name'],
                    phone=vd['phone'])
        user.set_password(vd['password'])
        user.save()
        return Response(UserSerializer(user).data)








