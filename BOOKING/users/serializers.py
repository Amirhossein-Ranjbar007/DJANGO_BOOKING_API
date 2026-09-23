from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError



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
        fields = ['email', 'phone', 'first_name', 'last_name', 'date_joined', 'is_staff']

        read_only_fields = ['date_joined', 'is_staff']


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=True, required=True)
    phone = serializers.CharField(max_length=11, required=True)
    password = serializers.CharField(required=True)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password_confirmation = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('wrong password!')
        return value



    def validate(self, data):
        if data['new_password'] != data['new_password_confirmation']:
            raise serializers.ValidationError ("passwords must be the same!")
        if data['new_password'] == data['old_password']:
            raise serializers.ValidationError('you need to choose a new password!')
        validate_password(data['new_password'], self.context['request'].user)
        return data


    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])  # instance=request.user
        instance.save()
        return instance

class UserLogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def create(self, validated_data):

        try:
            refresh_token = RefreshToken(validated_data['refresh_token'])
        except TokenError:
            raise serializers.ValidationError('Invalid refresh token!')

        token = refresh_token['user_id']
        user = self.context['request'].user
        if user.id == token:
            refresh_token.blacklist()
            return {}
        raise serializers.ValidationError ('something went wrong!')









