import unittest
import time

from passwordGenerator.password_gen.password_manager import PasswordManager

class TestPasswordFeatures(unittest.TestCase):
    def setUp(self):
        self.manager = PasswordManager()

    def test_pattern_password_structure(self):
        pattern = 'u{2}d{3}l{2}'
        password = self.manager.generate_pattern_password(pattern)
        self.assertTrue(password[0:2].isupper() and password[2:5].isdigit() and password[5:7].islower(), "Pattern structure is incorrect.")

    def test_vowel_password(self):
        pattern = 'v{10}'
        password = self.manager.generate_pattern_password(pattern)
        self.assertTrue(all(char in 'aeiou' for char in password), "Not all characters are lower-case vowels.")

    def test_consonant_password(self):
        pattern = 'c{10}'
        password = self.manager.generate_pattern_password(pattern)
        self.assertTrue(all(char in 'bcdfghjklmnpqrstvwxyz' for char in password), "Not all characters are lower-case consonants.")

    def test_special_characters_password(self):
        pattern = 's{10}'
        password = self.manager.generate_pattern_password(pattern)
        self.assertTrue(all(char in '!@#$%^&*()-_=+' for char in password), "Not all characters are special characters.")

    def test_random_password_length(self):
        length = 15
        password = self.manager.generate_random_password(length)
        self.assertEqual(len(password), length, "Random password length is incorrect.")

    def test_unique_passwords(self):
        passwords = set(self.manager.generate_random_password(10) for _ in range(100))
        self.assertEqual(len(passwords), 100, "Passwords are not unique.")

    def test_performance_large_scale_password_generation(self):
        start_time = time.time()
        for _ in range(1000):
            self.manager.generate_random_password(10)
        duration = time.time() - start_time
        self.assertLess(duration, 10, "Performance criteria not met.")

if __name__ == '__main__':
    unittest.main()
