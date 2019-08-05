import os

CACHES = {
    "default": {
         "BACKEND": "redis_cache.RedisCache",
         "LOCATION": os.environ.get('REDIS_URL'),
    }
}
  
