from django.middleware.cache import CacheMiddleware
from django.utils.cache import get_cache_key
from django.utils.decorators import decorator_from_middleware_with_args

class CustomCacheMiddleware(CacheMiddleware):

    def process_request(self, request):

        # try and get the cached GET response
        cache_key = get_cache_key(request, self.key_prefix, request.method, cache=self.cache)
        if cache_key is None:
            request._cache_update_cache = True
            return None  # No cache information available, need to rebuild.
        response = self.cache.get(cache_key)
        # if it wasn't found and we are looking for a HEAD, try looking just for that
        if response is None and request.method == "HEAD":
            cache_key = get_cache_key(
                request, self.key_prefix, "HEAD", cache=self.cache
            )
            response = self.cache.get(cache_key)

        if response is None:
            request._cache_update_cache = True
            return None  # No cache information available, need to rebuild.

        # hit, return cached response
        request._cache_update_cache = False
        return response


def cache_page(timeout, *, cache=None, key_prefix=None):
    return decorator_from_middleware_with_args(CustomCacheMiddleware)(
        page_timeout=timeout,
        cache_alias=cache,
        key_prefix=key_prefix,
    )