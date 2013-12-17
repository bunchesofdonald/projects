import unittest

from vowelcount import vowelcount


class TestVowelCount(unittest.TestCase):
    def test_vowelcount(self):
        """Vowel Count should count the number of vowels in the string"""
        expected = {}
        self.assertEqual(expected, vowelcount('z'))

        expected = {'e': 1, 'o': 1}
        self.assertEqual(expected, vowelcount('hello'))

        expected = {'e': 1, 'o': 2}
        self.assertEqual(expected, vowelcount('hello world'))
