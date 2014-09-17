import unittest
from app import utils
from collections import Counter

class TestWordCountUtils(unittest.TestCase):

    def setUp(self):
        pass

    def test_generate_random_text(self):
        text, words = utils.generate_random_text()
        for word in words.split():
            self.assertTrue(word in text)

    def test_get_exclusion_words(self):
        for i in range(10):
            text, ws = utils.generate_random_text()
            exclusion_words = utils.get_exclusion_words(text)
            self.assertTrue(len(exclusion_words) < len(text.split())
                and len(exclusion_words) > 0)

    def test_validate_word_count(self):
        # test 10 randomly generated text
        for i in range(10):
            text, words = utils.generate_random_text()
            cnt = Counter()
            for word in text.split():
                if word not in words.split():
                    cnt[word] += 1
            self.assertTrue(utils.validate_word_count(text, words, dict(cnt)))
