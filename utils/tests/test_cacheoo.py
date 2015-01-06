import unittest

from utils.cacheoo import Cache


class CacheooTestCase(unittest.TestCase):
    def test_clear(self):
        cache = Cache()

        cache.clear('test_key')
        self.assertFalse(cache.clear('test_key'))
        cache.write('test_key', 'test_value')
        self.assertTrue(cache.clear('test_key'))

    def test_is_cached(self):
        cache = Cache()

        cache.clear('test_key')
        self.assertFalse(cache.is_cached('test_key'))
        cache.write('test_key', 'test_value')
        self.assertTrue(cache.is_cached('test_key'))

    def test_write_read(self):
        cache = Cache()

        cache.write('test_key', 'test_value')
        self.assertEqual(cache.read('test_key'), 'test_value')
