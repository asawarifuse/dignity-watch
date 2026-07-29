"""Redis connection setup."""

import redis
from .config import settings

redis_client = redis.Redis.from_url(
    settings.redis_url,
    decode_responses=True,
)


def get_redis():
    """Dependency that provides Redis client."""
    return redis_client