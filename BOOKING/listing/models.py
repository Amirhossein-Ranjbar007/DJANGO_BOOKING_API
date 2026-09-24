from django.db import models
from users.models import HostProfile


class Category(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}:{self.slug}"


class SpaceStatus(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    ACTIVE = 'active', 'Active'
    INACTIVE = 'inactive', 'Inactive'


class SpacePriceUnit(models.TextChoices):
    HOUR = 'hour', 'Hourly'
    DAY = 'day', 'Daily'




class Amenity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Space(models.Model):

    host = models.ForeignKey(HostProfile, on_delete=models.CASCADE, related_name='host_space')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_host')
    amenities = models.ManyToManyField(Amenity, related_name='space_amenity')
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.PositiveIntegerField()
    price_unit = models.CharField(max_length=10, choices=SpacePriceUnit.choices, default=SpacePriceUnit.HOUR)
    city = models.CharField(max_length=200)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    status = models.CharField(max_length=20, choices=SpaceStatus.choices, default=SpaceStatus.DRAFT)

    def __str__(self):
        return f"{self.category.name}:{self.title}"


class SpaceImage(models.Model):

    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    image = models.ImageField()
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)





