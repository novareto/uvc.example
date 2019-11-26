import unittest
import uvcsite.testing
import uvc.example


my_layer = uvcsite.testing.BrowserLayer(uvc.example)


class TestAPI(unittest.TestCase):
    layer = my_layer

    def setUp(self):
        self.app = self.layer.create_application('app')

    def test_isThere(self):
        self.assertTrue('1', '1')
        browser = self.layer.new_browser('http://localhost/app')
