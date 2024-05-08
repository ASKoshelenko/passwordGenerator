import random
import string
import re


class PasswordManager:
    """
    Manages generation of passwords based on given specifications.
    """

    def generate_random_password(self, length=12, charset=string.ascii_letters + string.digits):
        """
        Generates a random password from the specified character set.

        Args:
            length (int): Length of the password to generate.
            charset (str): String of characters to use for generating the password.

        Returns:
            str: The generated random password.
        """
        return ''.join(random.choice(charset) for _ in range(length))

    def generate_pattern_password(self, pattern):
        """
        Generates a password based on a specific pattern.

        Args:
            pattern (str): A pattern string with format characters (d, l, L, p, u) followed by optional quantifiers in curly braces.

        Returns:
            str: The generated password based on the pattern.
        """
        result = ""
        # Improved regex to handle potential pattern errors more gracefully
        tokens = re.findall(r'([dlLpu])(?:\{(\d+)\})?', pattern)
        for char_type, count in tokens:
            count = int(count) if count else 1
            char_set = {
                'd': string.digits,
                'l': string.ascii_lowercase,
                'L': string.ascii_letters,
                'p': string.punctuation,
                'u': string.ascii_uppercase
            }.get(char_type, '')

            result += ''.join(random.choice(char_set) for _ in range(count))
        return result

