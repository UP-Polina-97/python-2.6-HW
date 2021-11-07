import pytest
import unittest
import requests
from main import yandex_disk_folder


class TestClassA(unittest.TestCase):
    def test_yandex_disk_folder(self):
        print('yandex_disk_folder')
        self.assertEqual(yandex_disk_folder(), 409)


