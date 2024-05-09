import random
import string
import re

class PasswordManager:
    SPECIAL_CHARACTERS = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    HEX_LOWER = '0123456789abcdef'
    HEX_UPPER = '0123456789ABCDEF'

    def __init__(self):
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
            part = ''.join(random.choice(char_set) for _ in range(count))
            result += part

        if 'H' in pattern and '-' in pattern:
            formatted_result = '-'.join(result[i:i + 2] for i in range(0, len(result), 2))
            return formatted_result[:17]
        return result

    def _expand_custom_sets(self, pattern):
        while '[' in pattern:
            start = pattern.index('[')
            end = pattern.index(']', start)
            content = pattern[start+1:end]

            if '|' in content:
                options = content.split('|')
                chosen_set = ''.join(random.choice(self.character_sets.get(option, option)) for option in options)
                replace_count = int(re.search(r'\{(\d+)\}', pattern[end+1:]).group(1)) if '{' in pattern[end:] else 1
                pattern = pattern.replace(pattern[start:end+1] + '{' + str(replace_count) + '}', chosen_set * replace_count)
            else:
                chosen_set = content
                replace_count = int(re.search(r'\{(\d+)\}', pattern[end+1:]).group(1)) if '{' in pattern[end:] else 1
                pattern = pattern.replace(pattern[start:end+1] + '{' + str(replace_count) + '}', chosen_set * replace_count)
        return pattern
