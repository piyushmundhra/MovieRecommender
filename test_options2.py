import unittest

from optpkg.rpkg.recommender import Recommender
from optpkg.userOptions import userOptions
from optpkg.options1 import Options1
from optpkg.Options2 import Options2

class TestOption2(unittest.TestCase):
    def test_IntTest1(self):
        uo1 = Options2()
        self.assertEqual(
            uo1.is_not_integer('f'),
            True,
            'Should be True'
        )
    def test_IntTest2(self):
        uo2 = Options2()
        self.assertEqual(
            uo2.is_not_integer('-'),
            True,
            'Should be True'
        )
    def test_IntTest3(self):
        uo3 = Options2()
        self.assertEqual(
            uo3.is_not_integer('1'),
            False,
            'Should be False'
        )     

unittest.main()