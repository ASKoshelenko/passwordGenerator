import logging
import os

def setup_logging(verbosity=0):
    """Set up logging with an optional verbosity level."""
    log_levels = {0: logging.INFO, 1: logging.INFO, 2: logging.DEBUG, 3: logging.DEBUG}
    log_level = log_levels.get(verbosity, logging.INFO)

    # Create logger
    logger = logging.getLogger('general')
    logger.setLevel(log_level)
    logger.handlers = [h for h in logger.handlers if not isinstance(h, logging.FileHandler)]  # Clean up file handlers if already exist

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # General log file
    log_file_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'log.txt')
    file_handler = logging.FileHandler(log_file_path, mode='a', encoding='utf-8', errors='ignore')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Debug logger for more verbose output
    debug_logger = logging.getLogger('debug')
    debug_log_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'debug.txt')
    debug_file_handler = logging.FileHandler(debug_log_path, mode='a', encoding='utf-8', errors='ignore')
    debug_file_handler.setFormatter(formatter)
    debug_logger.addHandler(debug_file_handler)
    debug_logger.setLevel(logging.DEBUG if verbosity > 0 else logging.NOTSET)

    return logger, debug_logger
