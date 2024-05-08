import unittest
from unittest.mock import patch, MagicMock
import logging
from passwordGenerator.config.logger import setup_logging

class TestCLI(unittest.TestCase):
    def setUp(self):
        """Setup for tests by removing all handlers from the root logger."""
        self.clear_logging_handlers()

    def tearDown(self):
        """Tear down test by closing and removing all handlers from the root logger."""
        self.clear_logging_handlers()

    def clear_logging_handlers(self):
        """Clears all handlers from the root logger."""
        logger = logging.getLogger()
        while logger.handlers:
            handler = logger.handlers[0]
            handler.close()
            logger.removeHandler(handler)

    @patch('logging.FileHandler')
    @patch('logging.StreamHandler')
    def test_logging_to_files(self, stream_handler_mock, file_handler_mock):
        """Test if logging to files is being performed correctly."""
        setup_logging(verbosity=0)  # Test with verbosity=0
        file_handler_mock.assert_called_once()
        stream_handler_mock.assert_not_called()  # No stream handler should be added at verbosity=0

        setup_logging(verbosity=2)  # Test with increased verbosity
        file_handler_mock.assert_called()
        stream_handler_mock.assert_called()  # Now it should add a stream handler

    @patch('logging.Logger.info')
    def test_verbose_logging_info(self, log_info_mock):
        """Test verbose logging at the INFO level."""
        logger = setup_logging(verbosity=1)
        logger.info("Test info message")
        log_info_mock.assert_called_with("Test info message")

    @patch('logging.Logger.debug')
    def test_verbose_logging_debug(self, log_debug_mock):
        """Test verbose logging at the DEBUG level."""
        logger = setup_logging(verbosity=2)
        logger.debug("Test debug message")
        log_debug_mock.assert_called_with("Test debug message")

if __name__ == '__main__':
    unittest.main()
