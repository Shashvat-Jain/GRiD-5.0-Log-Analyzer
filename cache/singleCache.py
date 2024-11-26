import redis
import json


class CacheServer:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis_client = redis.StrictRedis(host=host, port=port, db=db)

    def set_json(self, key, value, expire_time=None):
        """
        Set a JSON object in the cache.

        :param key: The key to set.
        :param value: The JSON object to store.
        :param expire_time: Optional expiration time for the key in seconds.
        """
        json_value = json.dumps(value)
        if expire_time is None:
            self.redis_client.set(key, json_value)
        else:
            self.redis_client.setex(key, expire_time, json_value)

    def get_json(self, key):
        """
        Get a JSON object associated with a key from the cache.

        :param key: The key to retrieve.
        :return: The JSON object associated with the key, or None if the key is not found or is not a valid JSON object.
        """
        json_value = self.redis_client.get(key)
        if json_value:
            try:
                return json.loads(json_value.decode('utf-8'))
            except json.JSONDecodeError:
                return None
        return None

    def delete(self, key):
        """
        Delete a key-value pair from the cache.

        :param key: The key to delete.
        """
        self.redis_client.delete(key)

    def keys(self, pattern='*'):
        """
        List keys matching a pattern in the cache.

        :param pattern: The pattern to match keys against (default is '*').
        :return: A list of keys matching the pattern.
        """
        return [key.decode('utf-8') for key in self.redis_client.keys(pattern)]

    def exists(self, key):
        """
        Check if a key exists in the cache.

        :param key: The key to check for existence.
        :return: True if the key exists, False otherwise.
        """
        return self.redis_client.exists(key)

    def flush(self):
        """
        Flush all keys from the cache (clear the cache).
        """
        self.redis_client.flushall()
