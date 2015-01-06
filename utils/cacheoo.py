# -*- coding: utf-8 -*-

import os
import time
import hashlib
import settings

from fileoo import File


class Cache:
    def __init__(self):
        self.fil = File()

    def fingerprint_path(self, key):
        fingerprint = hashlib.md5(key).hexdigest()
        cache_path = os.path.join(settings.CACHE_PATH, fingerprint + '.gz')
        return fingerprint, cache_path

    def is_cached(self, key):
        fingerprint, cache_path = self.fingerprint_path(key)

        if os.path.exists(cache_path) and \
           time.time() - os.path.getmtime(cache_path) < settings.CACHE_EXPIRE:
           return True
        return False

    def read(self, key):
        fingerprint, cache_path = self.fingerprint_path(key)

        if self.is_cached(key):
            return self.fil.read(cache_path, content_type='gz').next()

    def write(self, key, content):
        fingerprint, cache_path = self.fingerprint_path(key)
        return self.fil.write(cache_path, content, content_type='gz')
