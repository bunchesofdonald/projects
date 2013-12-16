import unittest

from reverse_string import reverse_string


class TestReverseString(unittest.TestCase):
    def test_string_is_reversed(self):
        """A String should be reversed"""
        expected = 'sracecar'
        self.assertEqual(expected, reverse_string('racecars'))

    def test_sentence_is_reversed(self):
        """A String with spaces should be reversed"""
        expected = 'tset a si siht'
        self.assertEqual(expected, reverse_string('this is a test'))
