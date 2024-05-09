import re
import random
import string

class PasswordManager:
    """
    Manages generation of passwords based on given specifications.
    """
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
        # Обработка пользовательских наборов символов и альтернативных выборов внутри квадратных скобок
        while '[' in pattern:
            start = pattern.index('[')
            end = pattern.index(']', start)
            content = pattern[start+1:end]

            # Обработка альтернативных наборов символов
            if '|' in content:
                options = content.split('|')
                chosen_set = random.choice(options)
            else:
                chosen_set = content

            # Замена паттерна на выбранный набор символов
            replace_count = int(pattern[end+2:end+4]) if '}' in pattern[end+1:] else 1
            pattern = pattern.replace(pattern[start:end+5], chosen_set * replace_count)

        # Генерация пароля по окончательному шаблону
        for char in pattern:
            if char in self.character_sets:
                result += random.choice(self.character_sets[char])
            else:
                result += char  # Добавляем символы как есть, если они не входят в наборы

        return result

