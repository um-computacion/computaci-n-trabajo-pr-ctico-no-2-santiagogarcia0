import unittest

def is_palindrome(text):
    text = text.lower()
    clean_text = ''.join(char for char in text if char.isalnum())
    return clean_text == clean_text[::-1]

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

if __name__ == "__main__":
    print("Detector de palíndromos")
    print("Ingresa una palabra o frase para verificar si es palíndromo.")
    print("Presiona Ctrl+C para salir.")

    try:
        while True:
            texto = input("\nTexto: ")
            if is_palindrome(texto):
                print("✅ Es un palíndromo.")
            else:
                print("❌ No es un palíndromo.")
    except KeyboardInterrupt:
        print("\nPrograma finalizado.")
