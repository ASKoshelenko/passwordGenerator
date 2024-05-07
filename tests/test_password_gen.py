import unittest
from passwordGenerator.password_gen.password_manager import PasswordManager

class TestPasswordManager(unittest.TestCase):
    def setUp(self):
        """Initialize the PasswordManager for use in each test."""
        self.manager = PasswordManager()

    def test_generate_random_password_length(self):
        """Test that the random password is generated with the specified length."""
        password = self.manager.generate_random_password(12)
        self.assertEqual(len(password), 12)

    def test_generate_pattern_password_output(self):
        """Test that a password is generated correctly from a pattern."""
        pattern = 'u{2}d{2}'
        password = self.manager.generate_pattern_password(pattern)
        self.assertTrue(password.isalnum())
        self.assertEqual(len(password), 4)

if __name__ == '__main__':
    unittest.main()
