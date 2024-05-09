import unittest
import time

from passwordGenerator.password_gen.password_manager import PasswordManager

class TestPasswordFeatures(unittest.TestCase):
    """
    Test suite for the functionality of the PasswordManager class.

    This class tests various features of password generation, including pattern-based password generation,
    random password generation, performance, and uniqueness checks.
    """

    def setUp(self):
        """
        Initialize resources before each test. In this case, an instance of PasswordManager.
        """
        self.manager = PasswordManager()

    def test_pattern_password_structure(self):
        """
        Tests if the generated password matches a specific pattern structure.

        Pattern 'u{2}d{3}l{2}' should result in two uppercase letters, followed by three digits,
        and ending with two lowercase letters.
        """
        pattern = 'u{2}d{3}l{2}'
        password = self.manager.generate_pattern_password(pattern)
        self.assertTrue(password[0:2].isupper() and password[2:5].isdigit() and password[5:7].islower(),
                        "Pattern structure is incorrect.")

    def test_vowel_password(self):
        """
        Tests if the generated password consists only of lowercase vowels as specified by the pattern 'v{10}'.
        """
        pattern = 'v{10}'
        password = self.manager.generate_pattern_password(pattern)
        self.assertTrue(all(char in 'aeiou' for char in password), "Not all characters are lower-case vowels.")

    def test_consonant_password(self):
        """
        Tests if the generated password consists only of lowercase consonants as specified by the pattern 'c{10}'.
        """
        pattern = 'c{10}'
        password = self.manager.generate_pattern_password(pattern)
        self.assertTrue(all(char in 'bcdfghjklmnpqrstvwxyz' for char in password),
                        "Not all characters are lower-case consonants.")

    def test_special_characters_password(self, SPECIAL_CHARACTERS="!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"):
        """
        Tests if the generated password consists only of special characters as specified by the pattern 's{10}'.
        """
        pattern = 's{10}'
        password = self.manager.generate_pattern_password(pattern)
        self.assertTrue(all(char in SPECIAL_CHARACTERS for char in password),
                        "Not all characters are special characters.")

    def test_random_password_length(self):
        """
        Verifies that the length of the randomly generated password matches the specified length.
        """
        length = 15
        password = self.manager.generate_random_password(length)
        self.assertEqual(len(password), length, "Random password length is incorrect.")

    def test_unique_passwords(self):
        """
        Checks the uniqueness of 100 randomly generated passwords of length 10.
        """
        passwords = set(self.manager.generate_random_password(10) for _ in range(100))
        self.assertEqual(len(passwords), 100, "Passwords are not unique.")

    def test_performance_large_scale_password_generation(self):
        """
        Measures the performance by generating 1000 passwords of length 10 and ensuring
        the operation completes within 10 seconds.
        """
        start_time = time.time()
        for _ in range(1000):
            self.manager.generate_random_password(10)
        duration = time.time() - start_time
        self.assertLess(duration, 10, "Performance criteria not met.")

if __name__ == '__main__':
    unittest.main()
