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

    # Создаем логгер
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Устанавливаем самый низкий уровень для логгера

    # Очищаем предыдущие обработчики, если они есть
    if logger.hasHandlers():
        logger.handlers.clear()

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(console_log_level)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(console_handler)

    # File handler setup if requested
    if write_to_file:
        file_handler = logging.FileHandler('logs.txt')
        file_level = levels.get(verbosity, logging.INFO)
        file_handler.setLevel(file_level)  # Установка уровня логирования для файла
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - Executed Command: "%(message)s"'))
        logger.addHandler(file_handler)

    return logger
