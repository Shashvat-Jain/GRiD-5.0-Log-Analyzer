import unittest
from your_cache_module import CacheServer  # Import your CacheServer class


class TestCacheServer(unittest.TestCase):
    def setUp(self):
        # Create a CacheServer instance for testing
        self.cache = CacheServer()

    def tearDown(self):
        # Cleanup: Flush the cache after each test
        self.cache.flush()

    def test_set_and_get_json(self):
        # Test setting and getting a JSON object in the cache
        data = {"name": "John Doe", "age": 30}
        self.cache.set_json("user:123", data)

        retrieved_data = self.cache.get_json("user:123")
        self.assertEqual(data, retrieved_data)

    def test_key_listing(self):
        # Test listing keys in the cache
        self.cache.set("key1", "value1")
        self.cache.set("key2", "value2")

        keys = self.cache.keys()
        self.assertIn("key1", keys)
        self.assertIn("key2", keys)

    def test_key_existence(self):
        # Test checking key existence in the cache
        self.cache.set("existing_key", "value")

        self.assertTrue(self.cache.exists("existing_key"))
        self.assertFalse(self.cache.exists("nonexistent_key"))

    def test_delete_key(self):
        # Test deleting a key from the cache
        self.cache.set("key_to_delete", "value")
        self.assertTrue(self.cache.exists("key_to_delete"))

        self.cache.delete("key_to_delete")
        self.assertFalse(self.cache.exists("key_to_delete"))


if __name__ == "__main__":
    unittest.main()
