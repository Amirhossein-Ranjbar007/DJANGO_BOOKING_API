from rest_framework.throttling import SimpleRateThrottle


class BookingCreateThrottle(SimpleRateThrottle):

    scope = 'book_create'

    def get_cache_key(self, request, view):
        return self.get_ident(request)


