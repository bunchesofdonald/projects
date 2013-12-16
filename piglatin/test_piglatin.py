import unittest

from piglatin import piglatin


class TestPigLatin(unittest.TestCase):
    def test_pig_latin_begin_consonant(self):
        """
        Words that begin with consonants should have them moved to the end
        and suffixed with 'ay'
        """
        expected = "appyhay"
        self.assertEqual(expected, piglatin("happy"))

        expected = "uckday"
        self.assertEqual(expected, piglatin("duck"))

        expected = "oveglay"
        self.assertEqual(expected, piglatin("glove"))

    def test_pig_latin_begin_vowel(self):
        """Words that begin with vowels should be suffixed with 'way' """
        expected = "eggway"
        self.assertEqual(expected, piglatin("egg"))

        expected = "inboxway"
        self.assertEqual(expected, piglatin("inbox"))

        expected = "eightway"
        self.assertEqual(expected, piglatin("eight"))

    def test_pig_latin_y(self):
        """
        'y' should be treated differently whether it starts the word or is
        in the middle.
        """
        expected = "ellowyay"
        self.assertEqual(expected, piglatin("yellow"))

        expected = "ythmrhay"
        self.assertEqual(expected, piglatin("rhythm"))
