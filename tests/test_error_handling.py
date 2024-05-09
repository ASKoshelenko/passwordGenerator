import unittest
from unittest.mock import patch
from io import StringIO

from passwordGenerator.cli.main import main


class TestCLIErrorHandling(unittest.TestCase):
    """
    Test suite for the CLI error handling of the password generator application.

    This class tests how the application handles unknown or invalid command-line arguments
    and ensures that appropriate error messages are displayed, and that the application exits correctly.
    """

    def test_unknown_argument(self):
        """
        Verifies that the CLI properly handles unrecognized command-line arguments.

        This test simulates passing an invalid argument and checks for the correct error message
        and termination of the application.

        Methodology:
        - Patches 'sys.argv' with test arguments including an invalid flag.
        - Captures output to 'sys.stdout' to examine what is printed to the console.
        - Expects the application to exit (SystemExit) due to unrecognized argument.
        - Asserts that the expected error message appears in the output.
        """
        test_args = ['cli.main', '-x']  # Simulating CLI input arguments
        with patch('sys.argv', test_args), patch('sys.stdout', new_callable=StringIO) as mocked_stdout:
            with self.assertRaises(SystemExit):  # Expecting the application to exit
                main()
            # Check for the expected error message in console output
            self.assertIn("Unknown arguments: ['-x']", mocked_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
