import unittest
from password_gen.pattern_password import generate_pattern_password
from password_gen.random_password import generate_random_password

class TestPasswordGen(unittest.TestCase):
    def test_random_password_length(self):
        """Тестирование длины случайного пароля."""
        length = 12
        password = generate_random_password(length)
        self.assertEqual(len(password), length)

    def test_pattern_password_output(self):
        """Тестирование генерации пароля по шаблону."""
        pattern = 'u{2}l{2}d{4}'
        password = generate_pattern_password(pattern)
        self.assertEqual(len(password), 8)
        self.assertTrue(any(char.isupper() for char in password))
        self.assertTrue(any(char.islower() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))

if __name__ == '__main__':
    unittest.main()
