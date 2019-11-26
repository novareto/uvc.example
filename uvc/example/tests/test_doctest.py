import unittest
import doctest
from uvc.example.tests.test_k import my_layer

class TestArithmetic(unittest.TestCase):

    def test_two_plus_two(self):
        self.assertEqual(2 + 2, 4)


def doctest_string_formatting():
    """Test Python string formatting

        >>> print('{} + {}'.format(2, 2))
        2 + 2

    """

def test_suite():
    suite = unittest.TestSuite([
        unittest.defaultTestLoader.loadTestsFromName(__name__),
        doctest.DocTestSuite(),
        doctest.DocFileSuite('../README.txt', optionflags=doctest.ELLIPSIS, globs={'layer': my_layer}),
                             
    ])
    suite.layer = my_layer
    return suite
