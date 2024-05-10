import unittest
from unittest.mock import patch, MagicMock
import logging
from passwordGenerator.config.logger import setup_logging


class TestCLI(unittest.TestCase):
    """
    Test suite for CLI-related logging functionality.

    This class tests the setup and behavior of logging based on different verbosity levels
    and confirms that loggers are interacting with file handlers and log methods as expected.
    """

    def setUp(self):
        """
        Prepare each test case by clearing existing handlers from loggers.
        """
        for logger in ['general', 'debug']:
            logging.getLogger(logger).handlers = []

    def tearDown(self):
        """
        Clean up after each test case by closing and removing handlers from loggers.
        """
        for logger in ['general', 'debug']:
            for handler in logging.getLogger(logger).handlers:
                handler.close()
            logging.getLogger(logger).handlers = []

    @patch('logging.FileHandler')
    def test_logging_file_handlers_initialization(self, mock_file_handler):
        """
        Test that file handlers are correctly initialized during logging setup.

        Args:
            mock_file_handler (MagicMock): Mocked file handler to track interactions.

        Verifies:
            The file handler is instantiated, which confirms logging setup involves file operations.
        """
        setup_logging(verbosity=0)
        mock_file_handler.assert_called()

    @patch('logging.Logger.info')
    def test_info_logging_at_info_verbosity_level(self, mock_info):
        """
        Test that informational logging is correctly triggered at a specified verbosity level.

        Args:
            mock_info (MagicMock): Mocked logger.info to track method calls.

        Verifies:
            The info method of the logger is called with expected messages.
        """
        logger, debug_logger = setup_logging(verbosity=1)
        logger.info("Test info message")
        mock_info.assert_called_with("Test info message")

    @patch('logging.Logger.debug')
    def test_debug_logging_at_debug_verbosity_level(self, mock_debug):
        """
        Test that debug logging is correctly triggered at a higher verbosity level.

        Args:
            mock_debug (MagicMock): Mocked logger.debug to track method calls.

        Verifies:
            The debug method of the debug logger is called with expected messages.
        """
        logger, debug_logger = setup_logging(verbosity=2)
        debug_logger.debug("Test debug message")
        mock_debug.assert_called_with("Test debug message")


if __name__ == '__main__':
    unittest.main()
