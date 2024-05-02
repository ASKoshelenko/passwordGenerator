import random
import string

def generate_pattern_password(pattern):
    result = []
    i = 0
    while i < len(pattern):
        char = pattern[i]

        if char == '\\':
            if i + 1 < len(pattern):
                result.append(pattern[i + 1])
                i += 2
                continue
            else:
                raise ValueError("Incomplete escape sequence at end of pattern.")

        elif char == '[':
            end = pattern.find(']', i + 1)
            if end == -1:
                raise ValueError("No closing ']' found for custom character set.")
            custom_set = pattern[i + 1:end]
            if '^' in custom_set:
                base, exclude = custom_set.split('^', 1)
                custom_set = ''.join(ch for ch in base if ch not in exclude)
            else:
                custom_set = custom_set

            i = end + 1

            if i < len(pattern) and pattern[i] == '{':
                rep_end = pattern.find('}', i + 1)
                if rep_end == -1:
                    raise ValueError("No closing '}' found for repetition specifier.")
                num = int(pattern[i + 1:rep_end])
                result.extend(random.choice(custom_set) for _ in range(num))
                i = rep_end  # Обновите индекс i для перехода за '}'
            else:
                result.append(random.choice(custom_set))

        elif char in 'dluLp':
            next_index = i + 1
            if next_index < len(pattern) and pattern[next_index] == '{':
                rep_end = pattern.find('}', next_index + 1)
                if rep_end == -1:
                    raise ValueError("No closing '}' found for repetition specifier.")
                num = int(pattern[next_index + 1:rep_end])
                func_map = {
                    'd': string.digits,
                    'l': string.ascii_lowercase,
                    'L': string.ascii_letters,
                    'u': string.ascii_uppercase,
                    'p': ".,;:"
                }
                result.extend(random.choice(func_map[char]) for _ in range(num))
                i = rep_end + 1
            else:
                func_map = {
                    'd': string.digits,
                    'l': string.ascii_lowercase,
                    'L': string.ascii_letters,
                    'u': string.ascii_uppercase,
                    'p': ".,;:"
                }
                result.append(random.choice(func_map[char]))
                i += 1
        else:
            raise ValueError(f"Unexpected pattern character '{char}' at position {i}.")
        i += 1  # Перемещение на следующий символ, если не было других изменений индекса

    return ''.join(result)

