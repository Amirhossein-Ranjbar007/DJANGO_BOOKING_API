from rest_framework import serializers
from.models import Category,Space,SpaceImage,Amenity





class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description', 'is_active']











