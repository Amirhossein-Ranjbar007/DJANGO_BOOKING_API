from rest_framework.throttling import SimpleRateThrottle
from random import randint


class RegisterThrottle(SimpleRateThrottle):

    scope = 'register'

    def get_cache_key(self, request, view):
        return self.get_ident(request)


class ProfileThrottle(SimpleRateThrottle):

    scope = 'profile'

    def get_cache_key(self, request, view):
        email = request.user.email
        phone = request.user.phone[4:7]
        indent = self.get_ident(request)
        return f"profile:{email}:{phone}:{indent}"

class ChangePasswordThrottle(SimpleRateThrottle):

    scope = 'change_password'
    def get_cache_key(self, request, view):
        email = request.user.email
        indent = self.get_ident(request)
        return f"change-password{email}:{indent}"



