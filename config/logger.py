import logging
import os

# Constants for log file paths
LOG_DIRECTORY = os.path.join(os.path.dirname(__file__), '..', 'logs')  # Directory for log files
GENERAL_LOG_FILE = 'password_generator.log'  # General log file name
DEBUG_LOG_FILE = 'password_generator.debug'  # Debug log file name

# Logging levels
LOG_LEVEL_INFO = 1  # Equivalent to logging.INFO
LOG_LEVEL_DEBUG = 2  # Equivalent to logging.DEBUG


def setup_logging(verbosity=0):
    """
    Configures and initializes logging for the application based on the given verbosity level.
    Sets up both a general logger and a debug logger with appropriate log files.

    Args:
        verbosity (int): The verbosity level of logging, where 0 is INFO by default and higher values enable DEBUG.

    Returns:
        tuple: A tuple containing two logging.Logger objects: (general_logger, debug_logger).
               - general_logger: for standard operational logs.
               - debug_logger: for detailed debug information, activated at higher verbosity levels.
    """
    log_levels = {
        0: logging.INFO,  # Default level
        LOG_LEVEL_INFO: logging.INFO,  # Info level
        LOG_LEVEL_DEBUG: logging.DEBUG  # Debug level
    }
    log_level = log_levels.get(verbosity, logging.INFO)  # Determine log level based on verbosity

    # Setting up the general logger
    general_logger = logging.getLogger('general')
    general_logger.setLevel(log_level)
    clear_handlers(general_logger)  # Avoid duplicate logging

    # Message format for logging
    formatter = logging.Formatter('%(asctime)s \t %(levelname)s \t %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # General log file setup
    general_log_path = os.path.join(LOG_DIRECTORY, GENERAL_LOG_FILE)
    file_handler = logging.FileHandler(general_log_path, mode='a', encoding='utf-8', errors='ignore')
    file_handler.setFormatter(formatter)
    general_logger.addHandler(file_handler)

    # Debug logger setup for more detailed output
    debug_logger = logging.getLogger('debug')
    debug_log_path = os.path.join(LOG_DIRECTORY, DEBUG_LOG_FILE)
    debug_file_handler = logging.FileHandler(debug_log_path, mode='a', encoding='utf-8', errors='ignore')
    debug_file_handler.setFormatter(formatter)
    debug_logger.addHandler(debug_file_handler)
    debug_logger.setLevel(logging.DEBUG if verbosity >= LOG_LEVEL_DEBUG else logging.NOTSET)

    return general_logger, debug_logger


def clear_handlers(logger):
    """
    Removes all handlers attached to the specified logger to prevent duplicate log entries.

    Args:
        logger (logging.Logger): The logger from which handlers will be removed.

    Returns:
        None: This function modifies the logger in-place and does not return a value.
    """
    while logger.handlers:
        handler = logger.handlers[0]
        handler.close()  # Properly close the handler
        logger.removeHandler(handler)  # Remove the handler from the logger
