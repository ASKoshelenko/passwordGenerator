import logging
import os

def setup_logging(verbosity=0):
    """Set up logging with an optional verbosity level."""
    log_levels = {0: logging.INFO, 1: logging.DEBUG, 2: logging.DEBUG, 3: logging.DEBUG}
    log_level = log_levels.get(verbosity, logging.INFO)

    logger = logging.getLogger()
    logger.setLevel(log_level)

    # Define formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Log to file by default
    log_file_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'log.txt')
    file_handler = logging.FileHandler(log_file_path, mode='a', encoding='utf-8', errors='ignore')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Conditionally log to console based on verbosity
    if verbosity > 0:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
