import random
import string

def generate_random_password(length, charset):
    """Generate a random password using specified charset."""
    return ''.join(random.choice(charset) for _ in range(length))

def generate_pattern_password(pattern):
    result = []
    i = 0
    while i < len(pattern):
        if pattern[i] == '\\':
            i += 1  # Переходим к следующему символу
            result.append(pattern[i])
        elif pattern[i] == 'd':
            result.append(random.choice(string.digits))
        elif pattern[i] == 'l':
            result.append(random.choice(string.ascii_lowercase))
        elif pattern[i] == 'u':
            result.append(random.choice(string.ascii_uppercase))
        elif pattern[i] == 'p':
            result.append(random.choice(".,;:"))
        elif pattern[i] == '[':
            # Находим закрывающую скобку и генерируем символ из кастомного набора
            close_bracket = pattern.find(']', i)
            custom_set = pattern[i+1:close_bracket]
            result.append(random.choice(custom_set))
            i = close_bracket
        # Добавить обработку повторов {n} (можно добавить позже)
        i += 1
    return ''.join(result)
