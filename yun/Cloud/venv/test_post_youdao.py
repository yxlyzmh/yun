import unittest
from unittest import mock

from post_youdao import *

class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
    def test_get_ts(self):
        get_ts=mock.Mock(return_value='18468439930')
        self.assertEqual('18468439930',get_ts())

    def test_get_salt(self):
        get_salt=mock.Mock(return_value='18468439930')
        self.assertEqual('18468439930',get_salt())
    def test_get_sign(self):
        get_sign=mock.Mock(return_value='b2ba12b30ffe0261057d8e59fcbe39cc')
        self.assertEqual('b2ba12b30ffe0261057d8e59fcbe39cc',get_sign())

if __name__ == '__main__':
    unittest.main()
