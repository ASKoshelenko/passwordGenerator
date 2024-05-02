import logging
import sys

def setup_logging(verbosity, write_to_file):
    """Configure logging to console and optionally to a file."""
    levels = {
        0: logging.WARNING,
        1: logging.INFO,
        2: logging.DEBUG,
        3: logging.NOTSET
    }
    console_log_level = levels.get(verbosity, logging.INFO)

    # Clear any existing handlers
    logging.getLogger().handlers = []

    # Console formatter
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(console_log_level)
    console_handler.setFormatter(console_formatter)
    logging.getLogger().addHandler(console_handler)

    # File handler setup if requested
    if write_to_file:
        file_formatter = logging.Formatter('%(asctime)s - Executed Command: "%(message)s"')
        file_handler = logging.FileHandler('test_results.txt')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(file_formatter)
        logging.getLogger().addHandler(file_handler)

    # Set the lowest logging level on logger
    logging.getLogger().setLevel(min(console_log_level, logging.INFO))
