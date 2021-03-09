import unittest

from optpkg.rpkg.recommender import Recommender
from optpkg.userOptions import userOptions
from optpkg.options1 import Options1
from optpkg.Options2 import Options2

class TestRec(unittest.TestCase):
    def test_imdbToMovie_firstMovie(self):
        r = Recommender()
        self.assertEqual(
           r.imdbToMovie('0114709'),
           1,
           "Should be 1"
        )

    def test_imdbToMovie_lastMovie(self):
        r = Recommender()
        self.assertEqual(
           r.imdbToMovie('0101726'),
           193609,
           "Should be 193609"
        )

    def test_imdbToMovie_generalCase(self):
        r = Recommender()
        self.assertEqual(
           r.imdbToMovie('2702724'),
           157312,
           "Should be 157312"
        )
    
    def test_hasMovie_letterCase(self):
        r = Recommender()
        self.assertEqual(
           r.has_movie('f'),
           False,
           "Should be False"
        )

    def test_hasMovie_symbolCase(self):
        r = Recommender()
        self.assertEqual(
           r.has_movie('-'),
           False,
           "Should be False"
        )


    def test_hasMovie_validCase(self):
        r = Recommender()
        self.assertEqual(
           r.has_movie('2702724'),
           True,
           "Should be True"
        )

    def test_hasMovie_nullCase(self):
        r = Recommender()
        self.assertEqual(
           r.has_movie('0'),
           False,
           "Should be False"
        )

    def test_hasMovie_invalidCase(self):
        r = Recommender()
        self.assertEqual(
           r.has_movie('270272443213'),
           False,
           "Should be False"
        )

unittest.main()