import unittest
import string

def is_palindrome(text):
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned




class TestIsPalindrome(unittest.TestCase):
    def test_simple(self):
        word = "ala"
        result = is_palindrome(word)
        self.assertTrue(result)

    def test_simple_two(self):
        word = "oso"
        result = is_palindrome(word)
        self.assertTrue(result)

    def test_no_palindrome(self):
        word = "hola"
        result = is_palindrome(word)
        self.assertFalse(result)

    def test_with_more_letters(self):
        word = "amaca"
        result = is_palindrome(word)
        self.assertFalse(result)

    def test_no_palindrome_complex(self):
        word = "amacaca"
        result = is_palindrome(word)
        self.assertFalse(result)

    def test_complex(self):
        word = "neuquen"
        result = is_palindrome(word)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
