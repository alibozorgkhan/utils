utils
=====

Basic utils for daily needs

##  Tests:

Run `python -m unittest discover --pattern=test_*.py`.

##  Settings:

Sample `utils/settings.py` file:

```
# -*- coding: utf-8 -*-

#   CACHEOO
CACHE_PATH = "/path/to/cache"
CACHE_EXPIRE = 60 * 60 * 24 * 33  # 30 days

#   DBOO
POSTGRES_CONFIG = {
    'host': 'db_host',
    'user': 'db_user',
    'password': 'db_pass',
    'dbname': 'db_name'
}

#   WEBOO
MY_IP = '1.1.1.1'
DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.8,fa;q=0.6',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Referer': 'http://www.google.com',
    'Cache-Control': 'max-age=0',
}

PROXY_USERNAME = "proxy_user"
PROXY_PASSWORD = "proxy_pass"
PROXIES = """
proxy1
proxy2
"""
```