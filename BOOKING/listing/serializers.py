from rest_framework import serializers
from.models import Category,Space,SpaceImage,Amenity





class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description', 'is_active']


class SpaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Space
        fields = ['title', 'category', 'host', 'city', 'price', 'price_unit', 'updated_at']










