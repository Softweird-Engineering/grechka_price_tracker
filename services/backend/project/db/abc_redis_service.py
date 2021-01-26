import aioredis

from abc import ABC


class AbstractKeyValueService(ABC):
    """
    Abstract service provides 2 base private methods:
    - get(key) -> value
    - set(key, value) -> value if success.
    """

    @classmethod
    async def _set(cls, key: str, value: str) -> bool:
        """
        Coroutine, implements setting the value by the key to Redis db.
        :param key: redis key string.
        :param value: redis value string\byte array.
        :return: True if succeed.
        """
        redis = await aioredis.create_redis_pool('redis://redis')
        await redis.set(key, value)
        redis.close()
        await redis.wait_closed()
        return True

    @classmethod
    async def _get(cls, key) -> str:
        """
        Coroutine, implements getting the value via the key.
        :param key: redis key string.
        :return: value, if succeed.
        """
        redis = await aioredis.create_redis_pool('redis://redis')
        val = await redis.get(key)
        redis.close()
        await redis.wait_closed()
        try:
            return val.decode("utf-8")
        except AttributeError:
            raise aioredis.RedisError
