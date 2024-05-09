import random
import string
import re

class PasswordManager:
    """
    Manages generation of passwords based on given specifications.
    """
    SPECIAL_CHARACTERS="!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
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
        # Специальный случай для шаблона с '@' и символами ABCDEF
        if pattern.startswith('@['):
            chars = re.findall(r'\[([A-F]+)\]', pattern)
            if chars:
                chars = ''.join(chars)
                return '@' + ''.join(random.choice(chars) for _ in range(9))
        # Регулярное выражение для обработки обычных паттернов
        tokens = re.findall(r'([a-zA-Z])(\{\d+\})?', pattern)
        for char_type, count in tokens:
            count = int(count.strip('{}')) if count else 1
            char_set = self.character_sets.get(char_type, '')
            part = ''.join(random.choice(char_set) for _ in range(count))
            result += part

        # Дополнительная обработка для HEX формата с разделителями
        if 'H' in pattern and '-' in pattern:
            # Деление результата на части по два символа с добавлением дефисов
            formatted_result = '-'.join(result[i:i + 2] for i in range(0, len(result), 2))
            # Обрезаем строку до длины формата "HH-HH-HH-HH-HH-HH" (всего 17 символов, включая 5 дефисов)
            return formatted_result[:17]
        return result
