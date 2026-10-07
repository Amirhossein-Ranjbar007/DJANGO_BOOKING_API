from .models import Booking
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.core.cache import cache
import time


@receiver([post_save, post_delete], sender=Booking)
def invalidate_booking_cache(sender, instance, **kwargs):
    cache.set(f"booking_ts_{instance.user_id}", time.time())




@receiver([post_save,post_delete], sender=Booking)
def invalidate_booking_details(sender, instance, **kwargs):
    cache_key = f"BookingDetail:{instance.id}:{instance.user.id}"
    cache.delete(cache_key)




