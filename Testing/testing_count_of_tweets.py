import unittest

# imports data from other file
from Obsolete.twitter_obsolete import testing_dfApi2

# clones the data
btctw_df = testing_dfApi2()

# checks for number of posts
numberOfPosts = len(btctw_df)


class TestPosts(unittest.TestCase):

    def test_post_anzahl(self):
        self.assertEqual(numberOfPosts, 5, "Should be five")


if __name__ == '__main__':
    unittest.main()
