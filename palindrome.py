def is_palindrome(text):
    text = text.lower()
    clean_text = ''.join(char for char in text if char.isalnum())
    return clean_text == clean_text[::-1]