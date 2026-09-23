from rest_framework import serializers
from .models import User



class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, required=True)
    phone = serializers.CharField(max_length=11, required=True)
    first_name = serializers.CharField(max_length=100, required=True)
    last_name = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(required=True, write_only=True)
    password_confirmation = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        """
            check password confirmation in this validator and return error if they are not the same.
        """
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError("passwords must be the same!")
        return data


    def create(self, validated_data):
        validated_data.pop('password_confirmation')

        user = User.objects.create_user(email=validated_data['email'],
        phone=validated_data['phone'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'],
        password=validated_data['password']
        )
        return user





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'phone', 'date_joined', 'is_staff']

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=True, required=True)
    phone = serializers.CharField(max_length=11, required=True)
    password = serializers.CharField(required=True)
