import re
import random
import string

def expand_pattern(pattern):
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

def generate_pattern_password(pattern):
    try:
        return expand_pattern(pattern)
    except Exception as e:
        print(f"Ошибка при обработке шаблона {pattern}: {e}")
        raise
