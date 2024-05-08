import sys
import argparse
import string
import os
from passwordGenerator.password_gen.password_manager import PasswordManager
from passwordGenerator.config.logger import setup_logging

# Default values as constants
DEFAULT_PASSWORD_LENGTH = 12
DEFAULT_CHARSET = string.ascii_letters + string.digits
DEFAULT_COUNT = 1

# Logging levels
LOG_LEVEL_INFO = 0
LOG_LEVEL_VERBOSE = 1
LOG_LEVEL_DEBUG = 2
LOG_LEVEL_MORE_VERBOSE = 3

def main():
    """
    Main execution function for the password generator tool.
    Parses command line arguments and triggers password generation based on the input parameters.
    """
    parser = argparse.ArgumentParser(description="Password Generator Tool", add_help=False)
    parser.add_argument('-n', '--length', type=int, default=DEFAULT_PASSWORD_LENGTH, help='Specifies the length of the password.')
    parser.add_argument('-S', '--charset', type=str, default=DEFAULT_CHARSET, help='Character set for the password.')
    parser.add_argument('-t', '--template', type=str, help='Specifies a template for generating passwords.')
    parser.add_argument('-c', '--count', type=int, default=DEFAULT_COUNT, help='Number of passwords to generate.')
    parser.add_argument('-v', '--verbose', action='count', default=LOG_LEVEL_INFO, help='Increases verbosity level.')
    parser.add_argument('-f', '--file', type=str, help='File with list of password patterns.')
    parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit.')

    args, unknown = parser.parse_known_args()

    if args.help:
        parser.print_help()
        sys.exit(0)

    if unknown:
        print(f"Unknown arguments: {unknown}. Please use '-h' option for help.")
        sys.exit(1)

    general_logger, debug_logger = setup_logging(args.verbose)
    pm = PasswordManager()

    try:
        if args.file:
            process_password_file(args, pm, general_logger, debug_logger)
        elif args.template:
            generate_from_template(args, pm, general_logger, debug_logger)
        else:
            generate_random_passwords(args, pm, general_logger, debug_logger)
    except Exception as e:
        general_logger.error(f"Error occurred: {str(e)}")
        debug_logger.error(f"Exception details: {str(e)}")
        sys.exit(1)

def process_password_file(args, pm, general_logger, debug_logger):
    """
    Processes a file containing password patterns and generates passwords accordingly.
    """
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', args.file)
    try:
        with open(file_path, 'r') as file:
            patterns = file.read().splitlines()
            for pattern in patterns:
                if pattern.strip():
                    for _ in range(args.count):
                        password = pm.generate_pattern_password(pattern.strip())
                        general_logger.info(f"Generated password from pattern: {pattern.strip()}")
                        debug_logger.debug(f"Pattern used: {pattern.strip()}, Password: {password}")
                        print(password)
    except FileNotFoundError:
        general_logger.error(f"File not found: {file_path}")
        print(f"File not found: {file_path}")
        sys.exit(1)

def generate_from_template(args, pm, general_logger, debug_logger):
    """
    Generates passwords based on a user-specified template.
    """
    for _ in range(args.count):
        password = pm.generate_pattern_password(args.template)
        general_logger.info(f"Generated password from template: {args.template}")
        debug_logger.debug(f"Template used: {args.template}, Password: {password}")
        print(password)

def generate_random_passwords(args, pm, general_logger, debug_logger):
    """
    Generates random passwords based on specified parameters.
    """
    for _ in range(args.count):
        password = pm.generate_random_password(args.length, args.charset)
        general_logger.info("Generated random password.")
        debug_logger.debug(f"Charset used: {args.charset}, Password: {password}")
        print(password)

if __name__ == '__main__':
    main()
