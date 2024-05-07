import random
import string
import re

class PasswordManager:
    def generate_random_password(self, length=12, charset=string.ascii_letters + string.digits):
        """Generate a random password from the specified character set."""
        return ''.join(random.choice(charset) for _ in range(length))

    def generate_pattern_password(self, pattern):
        """Generate a password based on a specific pattern."""
        result = ""
        tokens = re.findall(r'([dlLpu])(?:\{(\d+)\})?', pattern)
        for char_type, count in tokens:
            count = int(count) if count else 1
            if char_type == 'd':
                result += ''.join(random.choice(string.digits) for _ in range(count))
            elif char_type == 'l':
                result += ''.join(random.choice(string.ascii_lowercase) for _ in range(count))
            elif char_type == 'L':
                result += ''.join(random.choice(string.ascii_letters) for _ in range(count))
            elif char_type == 'p':
                result += ''.join(random.choice(string.punctuation) for _ in range(count))
            elif char_type == 'u':
                result += ''.join(random.choice(string.ascii_uppercase) for _ in range(count))
        return result
