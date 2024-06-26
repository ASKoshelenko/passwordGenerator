import random
import sys
import argparse
import string
import os

from passwordGenerator.password_gen.password_manager import PasswordManager
from passwordGenerator.config.logger import setup_logging

# Default settings for password generation
DEFAULT_LENGTH = 12  # Default length of the generated password
DEFAULT_CHARSET = string.ascii_letters + string.digits  # Default character set used for password generation
DEFAULT_COUNT = 1  # Default number of passwords to generate

# Logging verbosity levels for detailed control over logging output
LOG_LEVEL_INFO = 0
LOG_LEVEL_VERBOSE = 1
LOG_LEVEL_DEBUG = 2
LOG_LEVEL_DETAILED = 3

# Error and Warning codes
ERROR_UNKNOWN_ARGS = 1
ERROR_FILE_NOT_FOUND = 2
ERROR_EXCEPTION_OCCURRED = 3
WARNING_EMPTY_FILE = "Yours file is empty, chose another and try again"


def main():
    """
    Entry point of the password generator application.
    Processes command line arguments and manages the flow of the application based on these arguments.

    Returns:
        None: The function prints outputs directly and handles system exits.
    """
    parser = argparse.ArgumentParser(description="Password Generator Tool")
    parser.add_argument('-n', '--length', type=int, default=DEFAULT_LENGTH,
                        help='Specifies the length of the password.')
    parser.add_argument('-S', '--charset', type=str, default=DEFAULT_CHARSET,
                        help='Character set to use for password generation.')
    parser.add_argument('-t', '--template', type=str, help='Template for generating passwords based on a pattern.')
    parser.add_argument('-c', '--count', type=int, default=DEFAULT_COUNT, help='Number of passwords to generate.')
    parser.add_argument('-v', '--verbose', action='count', default=LOG_LEVEL_INFO,
                        help='Set the verbosity level of logging.')
    parser.add_argument('-f', '--file', type=str, help='Path to a file containing password patterns.')
    parser.add_argument('-r', '--randomize', action='store_true', help='Randomly permute characters of the password.')

    args, unknown_arguments = parser.parse_known_args()

    if unknown_arguments:
        print(f"Unknown arguments: {unknown_arguments}. Use '--help' for help.")
        sys.exit(ERROR_UNKNOWN_ARGS)

    general_logger, debug_logger = setup_logging(args.verbose)
    pm = PasswordManager()

    try:
        if args.file:
            process_password_file(args, pm, general_logger, debug_logger)
        elif args.template:
            passwords = generate_from_template(args, pm, general_logger, debug_logger)
            for password in passwords:
                if args.randomize:
                    password = ''.join(random.sample(password, len(password)))
                print(password)
        else:
            generate_random_passwords(args, pm, general_logger, debug_logger)
    except Exception as e:
        general_logger.error(f"Error occurred: {e}")
        debug_logger.error(f"Exception details: {e}")
        sys.exit(ERROR_EXCEPTION_OCCURRED)


def process_password_file(args, pm, general_logger, debug_logger):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', args.file)
    try:
        with open(file_path, 'r') as file:
            patterns = file.read().splitlines()
            if not patterns:
                general_logger.warning(f"No patterns found in file: {file_path}")
                print(WARNING_EMPTY_FILE)
            for pattern in patterns:
                if pattern.strip():
                    for _ in range(args.count):
                        password = pm.generate_pattern_password(pattern.strip())
                        general_logger.info(f"Generated password from pattern {pattern.strip()}")
                        debug_logger.debug(f"Generate from file {args.file} \t Used charset {args.charset}")
                        print(password)
    except FileNotFoundError:
        general_logger.error(f"File not found: {file_path}")
        print(f"File not found: {file_path}")
        sys.exit(ERROR_FILE_NOT_FOUND)


def generate_from_template(args, pm, general_logger, debug_logger):
    """
    Generates passwords from a specified template.

    Args:
        args (Namespace): Parsed command line arguments.
        pm (PasswordManager): Instance of PasswordManager to generate passwords.
        general_logger (Logger): Logger for general logging.
        debug_logger (Logger): Logger for detailed debug logging.

    Returns:
        list: A list of generated passwords.
    """
    passwords = []
    for _ in range(args.count):
        password = pm.generate_pattern_password(args.template)
        general_logger.info(f"Generated password from template {args.template}")
        debug_logger.debug(f"Template used {args.template} \t Used charset {args.charset}")
        passwords.append(password)
    return passwords


def generate_random_passwords(args, pm, general_logger, debug_logger):
    """
    Generates random passwords based on specified length and character set.

    Args:
        args (Namespace): Parsed command line arguments.
        pm (PasswordManager): Instance of PasswordManager for password generation.
        general_logger (Logger): Logger for general logging.
        debug_logger (Logger): Logger for detailed debug logging.

    Returns:
        None: Passwords are printed directly to the console.
    """
    for _ in range(args.count):
        password = pm.generate_random_password(args.length, args.charset)
        general_logger.info("Generated random password.")
        debug_logger.debug(f"Generated Random password \t Used charset {args.charset}")
        print(password)


if __name__ == '__main__':
    main()
