import unittest
from unittest import main
from unittest import TestCase
from optpkg.rpkg.recommender import Recommender
from optpkg.userOptions import userOptions
from optpkg.options1 import Options1
from optpkg.Options2 import Options2

class TestOption1(unittest.TestCase):
    def test1(self):
        uo = Options1()
        self.assertEqual(
            uo.is_not_integer('f'),
            True,
            'Should be True'
        )
    def test2(self):
        uo = Options1()
        self.assertEqual(
            uo.is_not_integer('-'),
            True,
            'Should be True'
        )
    def test3(self):
        uo = Options1()
        self.assertEqual(
            uo.is_not_integer('1'),
            False,
            'Should be False'
        )     


if __name__ == '__main__':
    unittest.main()