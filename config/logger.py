import logging
import os

def setup_logging(verbosity, write_to_file):
    """Настройка логгирования в консоль и, опционально, в файл."""
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
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_log_level)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(console_handler)

    # File handler setup if requested
    if write_to_file:
        # Установка абсолютного пути к файлу логов
        log_file_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'log.txt')
        file_handler = logging.FileHandler(log_file_path, encoding='utf-8', errors='ignore')
        file_handler.setLevel(levels.get(verbosity, logging.INFO))
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - Executed Command: "%(message)s"'))
        logger.addHandler(file_handler)

    return logger
