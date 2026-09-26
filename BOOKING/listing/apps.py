from django.apps import AppConfig


class ListingConfig(AppConfig):
    name = 'listing'

    def ready(self):
        from . import signals