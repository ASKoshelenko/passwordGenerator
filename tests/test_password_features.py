import unittest
import time

from passwordGenerator.password_gen.password_manager import PasswordManager

class TestPasswordFeatures(unittest.TestCase):
    def setUp(self):
        """Setup for each test case."""
        self.manager = PasswordManager()

    def test_random_password_length(self):
        """Test that the random password has the correct length."""
        length = 15
        password = self.manager.generate_random_password(length=length)
        self.assertEqual(len(password), length, f"Password length should be {length}")

    def test_pattern_password_structure(self):
        """Test that the password matches the defined pattern."""
        pattern = 'u{2}d{3}l{2}'
        password = self.manager.generate_pattern_password(pattern)
        self.assertTrue(password[0:2].isupper(), "First 2 characters should be uppercase letters.")
        self.assertTrue(password[2:5].isdigit(), "Next 3 characters should be digits.")
        self.assertTrue(password[5:7].islower(), "Last 2 characters should be lowercase letters.")

    def test_unique_passwords(self):
        """Test that multiple generated passwords are unique."""
        passwords = set()
        num_passwords = 100  # Generate 100 passwords
        for _ in range(num_passwords):
            password = self.manager.generate_random_password(10)
            passwords.add(password)
        self.assertEqual(len(passwords), num_passwords, "All generated passwords should be unique.")

    def test_performance_large_scale_password_generation(self):
        """Test that the password generator can handle large-scale operations efficiently."""
        start_time = time.time()
        for _ in range(1000):  # Generate 1000 passwords
            self.manager.generate_random_password(10)
        end_time = time.time()
        duration = end_time - start_time
        self.assertLess(duration, 10, "Generating 1000 passwords should take less than 10 seconds")


if __name__ == '__main__':
    unittest.main()
