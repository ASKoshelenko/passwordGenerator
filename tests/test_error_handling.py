import unittest
from unittest.mock import patch
from io import StringIO

from passwordGenerator.cli.main import main

class TestCLIErrorHandling(unittest.TestCase):
    def test_unknown_argument(self):
        test_args = ['cli.main', '-x']
        with patch('sys.argv', test_args), patch('sys.stdout', new_callable=StringIO) as mocked_stdout:
            with self.assertRaises(SystemExit):
                main()
            self.assertIn("Unknown arguments: ['-x']", mocked_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
