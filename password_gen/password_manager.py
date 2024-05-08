import random
import string
import re

class PasswordManager:
    """
    Manages generation of passwords based on given specifications.
    """
    VOWELS = 'aeiouAEIOU'
    CONSONANTS = ''.join(c for c in string.ascii_letters if c.lower() not in 'aeiou')
    SPECIAL_CHARACTERS = '!@#$%^&*()-_=+'

    def __init__(self):
        self.character_sets = {
            'd': string.digits,
            'l': string.ascii_lowercase,
            'L': string.ascii_letters,
            'p': string.punctuation,
            'u': string.ascii_uppercase,
            'v': self.VOWELS.lower(),
            'V': self.VOWELS,
            'C': self.CONSONANTS,
            's': self.SPECIAL_CHARACTERS
        }

    def generate_random_password(self, length=12, charset=string.ascii_letters + string.digits):
        return ''.join(random.choice(charset) for _ in range(length))

    def generate_pattern_password(self, pattern):
        result = ""
        tokens = re.findall(r'([dlLpuvVCs])(\{\d+\})?', pattern)
        for char_type, count in tokens:
            count = int(count.strip('{}')) if count else 1
            char_set = self.character_sets.get(char_type, '')
            result += ''.join(random.choice(char_set) for _ in range(count))
        return result

# Ensure that all directory paths and imports in your test and main modules are correct and properly structured.
