import logging
import os

# Константы путей для файлов логгирования
LOG_DIRECTORY = os.path.join(os.path.dirname(__file__), '..', 'logs')
GENERAL_LOG_FILE = 'log.txt'
DEBUG_LOG_FILE = 'debug.txt'

# Уровни логгирования
LOG_LEVEL_INFO = 1
LOG_LEVEL_DEBUG = 2


def setup_logging(verbosity=0):
    """
    Configures logging for the application with optional verbosity level.

    Args:
        verbosity (int): The verbosity level. 0 - default (INFO), higher values increase verbosity.

    Returns:
        tuple: Tuple containing the general logger and debug logger.
    """
    log_levels = {
        0: logging.INFO,
        LOG_LEVEL_INFO: logging.INFO,
        LOG_LEVEL_DEBUG: logging.DEBUG
    }
    log_level = log_levels.get(verbosity, logging.INFO)

    # Настройка основного логгера
    general_logger = logging.getLogger('general')
    general_logger.setLevel(log_level)
    clear_handlers(general_logger)

    # Форматирование сообщений
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Основной файл журнала
    general_log_path = os.path.join(LOG_DIRECTORY, GENERAL_LOG_FILE)
    file_handler = logging.FileHandler(general_log_path, mode='a', encoding='utf-8', errors='ignore')
    file_handler.setFormatter(formatter)
    general_logger.addHandler(file_handler)

    # Журнал отладки для более подробного вывода
    debug_logger = logging.getLogger('debug')
    debug_log_path = os.path.join(LOG_DIRECTORY, DEBUG_LOG_FILE)
    debug_file_handler = logging.FileHandler(debug_log_path, mode='a', encoding='utf-8', errors='ignore')
    debug_file_handler.setFormatter(formatter)
    debug_logger.addHandler(debug_file_handler)
    debug_logger.setLevel(logging.DEBUG if verbosity >= LOG_LEVEL_DEBUG else logging.NOTSET)

    return general_logger, debug_logger


def clear_handlers(logger):
    """
    Clears all handlers from the specified logger to prevent duplicate logs.

    Args:
        logger (logging.Logger): The logger from which to remove all handlers.
    """
    while logger.handlers:
        handler = logger.handlers[0]
        handler.close()
        logger.removeHandler(handler)
