from rest_framework import serializers
from.models import Category,Space,SpaceImage,Amenity





class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description', 'is_active']



class SpaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Space
        fields = ['title', 'category__name', 'host__name', 'city', 'price', 'price_unit', 'updated_at']




class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['name']



class ImageSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceImage
        fields = ['image', 'is_primary']



class SpaceDetailSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(source='category.name')
    host_name = serializers.CharField(source='host.name')
    amenities = AmenitySerializer(many=True, read_only=True)
    images = ImageSpaceSerializer(many=True, read_only=True)

    class Meta:
        model = Space
        fields = ['title', 'category_name', 'host_name', 'amenities', 'city', 'capacity', 'price', 'price_unit',
                  'status', 'description', 'created_at', 'updated_at', 'images']



class SpaceCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Space
        fields = fields = [
            'title', 'category', 'description', 'city', 'address', 'capacity', 'price', 'price_unit',
            'latitude', 'longitude']











