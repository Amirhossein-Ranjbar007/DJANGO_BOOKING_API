from django.contrib import admin
from.models import Category,Space,SpaceImage,Amenity





@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'is_active']
    search_fields = ['name', 'slug']
    list_filter = ['is_active']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):

    list_display = ['category', 'host', 'title', 'status', 'created_at', 'updated_at']
    search_fields = ['title', 'host__display_name']
    list_filter = ['status']



@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):

    list_display = ['name']
    search_fields = ['name']




@admin.register(SpaceImage)
class SpaceImageAdmin(admin.ModelAdmin):

    list_display = ['space__display_name', 'created_at', 'is_primary']
    search_fields = ['space__title']
    list_filter = ['is_primary']









