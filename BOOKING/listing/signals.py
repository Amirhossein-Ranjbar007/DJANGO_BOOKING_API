from django.db.models.signals import post_save,post_delete,m2m_changed
from django.dispatch import receiver
from .models import Space
from django.core.cache import cache


@receiver([post_save,post_delete], sender=Space)
def Invalidate_Space_detail_cache(sender, instance, **kwargs):

    cache_key = f"space-detail:{instance.id}"
    cache.delete(cache_key)


@receiver(m2m_changed, sender=Space.amenities.through)
def invalidate_space_amenities_cache(sender, instance, **kwargs):

    cache_key = f"space-detail:{instance.id}"
    cache.delete(cache_key)
