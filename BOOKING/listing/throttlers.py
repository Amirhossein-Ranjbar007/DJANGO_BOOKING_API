from rest_framework.throttling import SimpleRateThrottle



class SpaceCreateThrottle(SimpleRateThrottle):

    scope = 'space_create'

    def get_cache_key(self, request, view):
        email = request.user.email
        indent = self.get_ident()
        return f"space-create:{email}:{indent}"


class SpaceUpdateThrottle(SimpleRateThrottle):

    scope = 'space_update'

    def get_cache_key(self, request, view):
        email = request.user.email
        indent = self.get_ident()
        return f"space-create:{email}:{indent}"

class SpaceDeleteThrottle(SimpleRateThrottle):

    scope = 'space-delete'

    def get_cache_key(self, request, view):
        return self.get_ident(request)


class HostProfileThrottle(SimpleRateThrottle):

    scope = 'host-profile'

    def get_cache_key(self, request, view):
        return self.get_ident(request)



