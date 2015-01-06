import os
import uuid
import unittest

from utils.fileoo import File


class FileooTestCase(unittest.TestCase):
    def test_read_write(self):
        fil = File()

        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, str(uuid.uuid4()))

        try:
            os.remove(file_path)
            return True
        except OSError:
            return False

        fil.write(file_path, 'test_content')
        self.assertTrue(os.path.exists(file_path))
        self.assertEqual(os.path.exists(file_path), fil.exists(file_path))
        self.assertEqual(fil.read(file_path), 'test_content')
