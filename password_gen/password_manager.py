import random
import string
import re


class PasswordManager:
    """
    Manages password generation based on predefined character sets and custom pattern inputs.
    Supports both random and pattern-based password generation with a variety of character options.
    """
    DEFAULT_LENGTH = 12
    SPECIAL_CHARACTERS = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    HEX_LOWER = '0123456789abcdef'
    HEX_UPPER = '0123456789ABCDEF'

    def __init__(self):
        """
        Initializes the PasswordManager with a dictionary of character sets for password generation.
        """
        self.character_sets = {
            'd': string.digits,
            'l': string.ascii_lowercase,
            'L': string.ascii_letters,
            'p': string.punctuation,
            'u': string.ascii_uppercase,
            'a': string.ascii_lowercase + string.digits,
            'A': string.ascii_letters + string.digits,
            'U': string.ascii_uppercase + string.digits,
            'h': self.HEX_LOWER,
            'H': self.HEX_UPPER,
            'v': 'aeiou',
            'V': 'aeiouAEIOU',
            'Z': 'AEIOU',
            'c': ''.join(c for c in string.ascii_lowercase if c not in 'aeiou'),
            'C': ''.join(c for c in string.ascii_letters if c.lower() not in 'aeiou'),
            'z': ''.join(c for c in string.ascii_uppercase if c not in 'AEIOU'),
            'b': '()[]{}<>',
            's': self.SPECIAL_CHARACTERS,
            'S': string.printable.strip(),
            'x': ''.join(chr(i) for i in range(0xA1, 0x100) if i != 0xAD),
        }

    @staticmethod
    def generate_random_password(length=DEFAULT_LENGTH, charset=string.ascii_letters + string.digits):
        """
        Generates a random password of a specified length using a specified character set.

        Args: length (int): The length of the password to be generated. Defaults to DEFAULT_LENGTH. charset (str):
        The set of characters to use for generating the password. Defaults to a combination of letters and digits.

        Returns:
            str: The generated random password.
        """
        return ''.join(random.choice(charset) for _ in range(length))



    # def generate_pattern_password(self, pattern):
    #     """
    #     Generates a password based on a specified pattern. The pattern can include character set indicators and
    #     length specifiers.
    #
    #     Args:
    #         pattern (str): The pattern string used to generate the password.
    #
    #     Returns:
    #         str: The generated password following the specified pattern.
    #     """
    #     result = ""
    #     if pattern.startswith('@['):
    #         # Special handling for patterns like '@[ABCDEF]{9}'
    #         char_set = re.findall(r'\[([A-F]+)\]', pattern)
    #         if char_set:
    #             #TODO rewrite range(9)
    #             return '@' + ''.join(random.choice(char_set[0]) for _ in range(9))
    #
    #     pattern = self._expand_custom_sets(pattern)
    #     tokens = re.findall(r'([a-zA-Z])(\{\d+\})?', pattern)
    #     for char_type, count in tokens:
    #         count = int(count.strip('{}')) if count else 1
    #         char_set = self.character_sets.get(char_type, '')
    #         part = ''.join(random.choice(char_set) for _ in range(count))
    #         result += part
    #
    #     if 'H' in pattern and '-' in pattern:
    #         formatted_result = '-'.join(result[i:i + 2] for i in range(0, len(result), 2))
    #         return formatted_result[:17]
    #     return result

    def _expand_custom_sets(self, pattern):
        """
        Expands custom sets defined within square brackets and applies repetition as specified in the pattern.

        Args:
            pattern (str): The pattern containing custom sets and optional repetition specifications.

        Returns:
            str: The pattern with expanded custom sets replaced directly in the string.
        """
        while '[' in pattern:
            start = pattern.index('[')
            end = pattern.index(']', start)
            content = pattern[start + 1:end]

            # Find the repetition count following the character set
            count_match = re.search(r"\{(\d+)\}", pattern[end + 1:])
            replace_count = int(count_match.group(1)) if count_match else 1

            if '|' in content:
                options = content.split('|')
                # Select a random option and repeat it replace_count times
                chosen_set = ''.join(random.choice(self.character_sets.get(option, option)) for option in options)
                replacement = ''.join(chosen_set for _ in range(replace_count))
                pattern = pattern.replace(pattern[start:end + 1 + len(count_match.group(0))], replacement)
            else:
                chosen_set = ''.join(self.character_sets.get(content, content))
                replacement = ''.join(chosen_set for _ in range(replace_count))
                pattern = pattern.replace(pattern[start:end + 1 + len(count_match.group(0))], replacement)

        return pattern
