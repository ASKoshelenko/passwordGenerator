import unittest
from unittest.mock import patch, mock_open, ANY
from io import StringIO
from passwordGenerator.cli.main import main as cli_main

class TestCLI(unittest.TestCase):
    def test_cli_random_password_default_length(self):
        """Test that the CLI generates a random password with the default length."""
        test_args = ['cli.main', '-n', '12']
        with patch('sys.argv', test_args), patch('sys.stdout', new_callable=StringIO) as mocked_out:
            cli_main()
            output = mocked_out.getvalue()
            self.assertIn('Generated Password:', output)
            self.assertEqual(len(output.strip().split(': ')[-1]), 12)

    def test_cli_verbose_logging(self):
        """Test the CLI verbose logging and file writing."""
        test_args = ['cli.main', '-vvv', '-w']
        with patch('sys.argv', test_args), patch('builtins.open', mock_open()) as mocked_file:
            cli_main()
            mocked_file.assert_called_with('/Users/ask/PycharmProjects/passGen/passwordGenerator/logs/log.txt', 'a',
                                           encoding='utf-8', errors='ignore')

if __name__ == '__main__':
    unittest.main()