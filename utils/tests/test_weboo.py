import unittest

from utils import settings
from utils.weboo import Web


class WebooTestCase(unittest.TestCase):
    def test_ip(self):
        web = Web()
        self.assertEqual(web.ip(), settings.MY_IP)
