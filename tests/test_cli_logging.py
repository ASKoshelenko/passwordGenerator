import unittest
from unittest.mock import patch, MagicMock
import logging
from passwordGenerator.config.logger import setup_logging

class TestCLI(unittest.TestCase):
    def setUp(self):
        for logger in ['general', 'debug']:
            logging.getLogger(logger).handlers = []

    def tearDown(self):
        for logger in ['general', 'debug']:
            for handler in logging.getLogger(logger).handlers:
                handler.close()
            logging.getLogger(logger).handlers = []

    @patch('logging.FileHandler')
    def test_logging_to_files(self, mock_file_handler):
        setup_logging(verbosity=0)
        mock_file_handler.assert_called()

    @patch('logging.Logger.info')
    def test_verbose_logging_info(self, mock_info):
        logger, debug_logger = setup_logging(verbosity=1)
        logger.info("Test info message")
        mock_info.assert_called_with("Test info message")

    @patch('logging.Logger.debug')
    def test_verbose_logging_debug(self, mock_debug):
        logger, debug_logger = setup_logging(verbosity=2)
        debug_logger.debug("Test debug message")
        mock_debug.assert_called_with("Test debug message")

if __name__ == '__main__':
    unittest.main()
