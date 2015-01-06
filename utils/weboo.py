# -*- coding: utf-8 -*-

import requests
import settings
import random

from requests.auth import HTTPProxyAuth
from cacheoo import Cache


class Web:
    def __init__(self):
        self.proxies = [p.strip() for p in settings.PROXIES.split('\n') if p.strip()]
        self.cacher = Cache()

    def read(self, url, headers=None, cookies=None, proxy=None, random_proxy=False, force_download=False, verify=True):
        if not force_download:
            if self.cacher.is_cached(url):
                return self.cacher.read(url)

        request_args = {
            'verify': verify
        }
        request_args['headers'] = headers or settings.DEFAULT_HEADERS

        if cookies:
            request_args['cookies'] = cookies

        if proxy:
            request_args['proxies'] = {"http": 'http://' + proxy}
        elif random_proxy:
            request_args['proxies'] = {"http": 'http://' + random.choice(self.proxies)}

        if proxy or random_proxy:
            request_args['auth'] = HTTPProxyAuth(settings.PROXY_USERNAME, settings.PROXY_PASSWORD)

        r = requests.get(url, **request_args)

        self.cacher.write(url, r.content)

        return r.content

    def ip(self, proxy=None, random_proxy=False):
        r = self.get('http://ip.42.pl/raw', proxy=proxy, random_proxy=random_proxy)
        return r.content
