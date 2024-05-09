import random
import string
import re

class PasswordManager:
    """
    Manages generation of passwords based on given specifications.
    """
    SPECIAL_CHARACTERS = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    HEX_LOWER = '0123456789abcdef'
    HEX_UPPER = '0123456789ABCDEF'

    def __init__(self):
        # Expanded character sets
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

    def generate_random_password(self, length=12, charset=string.ascii_letters + string.digits):
        return ''.join(random.choice(charset) for _ in range(length))

    def generate_pattern_password(self, pattern):
        result = ""
        pattern = self._expand_custom_sets(pattern)

        tokens = re.findall(r'([a-zA-Z])(\{\d+\})?', pattern)
        for char_type, count in tokens:
            count = int(count.strip('{}')) if count else 1
            char_set = self.character_sets.get(char_type, '')
            result += ''.join(random.choice(char_set) for _ in range(count))

        return result

    def _expand_custom_sets(self, pattern):
        while '[' in pattern:
            start = pattern.index('[')
            end = pattern.index(']', start)
            content = pattern[start+1:end]

            if '|' in content:
                options = content.split('|')
                chosen_option = random.choice(options)
                chosen_set = self.character_sets.get(chosen_option.strip(), chosen_option.strip())
                pattern = pattern.replace(pattern[start:end+1], chosen_set * 10)
            else:
                chosen_set = ''.join(self.character_sets.get(c, c) for c in content)
                pattern = pattern.replace(pattern[start:end+1], chosen_set)

        return pattern


