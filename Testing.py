import unittest

# importieren der TwitterApi.py
from TwitterApi import testing_dfApi2

# importiert die zu testende Pandas-Dateien (pd) von TwitterApi.py
btctw_df = testing_dfApi2()

# Testing ob wirklich 5 Kommentare geladen wurden
numberOfPosts = len(btctw_df)


class TestPosts(unittest.TestCase):

    def test_post_anzahl(self):
        self.assertEqual(numberOfPosts, 5, "Es sollten 5 Posts angezeigt werden")


if __name__ == '__main__':
    unittest.main()
