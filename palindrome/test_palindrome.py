import unittest

from palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_palindrome_is_palindrome(self):
        """is_palindrome should recognize a palindrome"""
        expected = True
        self.assertEqual(expected, is_palindrome('racecar'))

    def test_non_palindrome_is_not_palindrome(self):
        """is_palindrome should not think a non-palindrome is a palindrome"""
        expected = False
        self.assertEqual(expected, is_palindrome('not a palindrome'))
