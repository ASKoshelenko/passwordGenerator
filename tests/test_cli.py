import unittest
import subprocess

class TestCLI(unittest.TestCase):
    def test_cli_basic_functionality(self):
        """Тестирование базовой функциональности CLI."""
        result = subprocess.run(['python', '-m', 'cli.main', '-n', '10'], capture_output=True, text=True)
        self.assertTrue(result.stdout.startswith('Generated Password:'))
        self.assertEqual(len(result.stdout.strip().split(': ')[1]), 10)

    def test_cli_pattern_functionality(self):
        """Тестирование функциональности шаблонов CLI."""
        result = subprocess.run(['python', '-m', 'cli.main', '-t', 'd{4}'], capture_output=True, text=True)
        password = result.stdout.strip().split(': ')[1]
        self.assertEqual(len(password), 4)
        self.assertTrue(password.isdigit())

if __name__ == '__main__':
    unittest.main()
