import random
import string
import re

class PasswordManager:
    """
    Manages generation of passwords based on given specifications.
    """
    VOWELS = 'aeiouAEIOU'  # Combined upper and lower vowels
    CONSONANTS = ''.join([c for c in string.ascii_letters if c.lower() not in 'aeiou'])  # Combined upper and lower consonants
    SPECIAL_CHARACTERS = '!@#$%^&*()-_=+'

    def __init__(self):
        # Predefined character sets updated with correct keys
        self.character_sets = {
            'd': string.digits,
            'l': string.ascii_lowercase,
            'u': string.ascii_uppercase,
            'p': string.punctuation,
            'v': self.VOWELS,  # Corrected key for vowels
            'c': self.CONSONANTS,  # Corrected key for consonants
            's': self.SPECIAL_CHARACTERS,  # Corrected key for special characters
        }

    def generate_random_password(self, length=12, charset=string.ascii_letters + string.digits):
        """
        Generates a random password from the specified character set.
        """
        return ''.join(random.choice(charset) for _ in range(length))

    def generate_pattern_password(self, pattern):
        """
        Generates a password based on a specific pattern.
        """
        result = ""
        # Improved regex to handle potential pattern errors more gracefully
        tokens = re.findall(r'([dlupcsv])(?:\{(\d+)\})?', pattern)
        for char_type, count in tokens:
            count = int(count) if count else 1
            char_set = self.character_sets.get(char_type, '')
            result += ''.join(random.choice(char_set) for _ in range(count))
        return result

    def _expand_custom_sets(self, pattern):
        # Expanding custom sets like [abc]{5}
        while '[' in pattern:
            start = pattern.index('[')
            end = pattern.index(']', start)
            custom_set = pattern[start+1:end]
            custom_set = ''.join(sorted(set(custom_set)))  # Remove duplicate characters
            pattern = pattern.replace(pattern[start:end+1], custom_set)
        return pattern
