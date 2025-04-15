import unittest
from palindrome import is_palindrome

class TestSimplePalindromes(unittest.TestCase):
    def test_single_word_palindrome(self):
        self.assertTrue(is_palindrome("radar"))

    def test_single_word_non_palindrome(self):
        self.assertFalse(is_palindrome("python"))

class TestEdgeCases(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

    def test_case_insensitivity(self):
        self.assertTrue(is_palindrome("RaceCar"))

    def test_spaces_and_punctuation(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))

if __name__ == '__main__':
    unittest.main()
