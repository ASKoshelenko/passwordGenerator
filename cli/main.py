import random
import sys
import argparse
import string
import os
from passwordGenerator.password_gen.password_manager import PasswordManager
from passwordGenerator.config.logger import setup_logging

# Default settings
DEFAULT_LENGTH = 12
DEFAULT_CHARSET = string.ascii_letters + string.digits
DEFAULT_COUNT = 1

# Logging verbosity levels
LOG_LEVEL_INFO = 0
LOG_LEVEL_VERBOSE = 1
LOG_LEVEL_DEBUG = 2
LOG_LEVEL_DETAILED = 3

def main():
    """
    Entry point of the password generator application.
    It processes command line arguments and directs the flow of the application based on those arguments.
    """
    parser = argparse.ArgumentParser(description="Password Generator Tool")
    parser.add_argument('-n', '--length', type=int, default=DEFAULT_LENGTH, help='Specifies the length of the password.')
    parser.add_argument('-S', '--charset', type=str, default=DEFAULT_CHARSET, help='Character set to use for password generation.')
    parser.add_argument('-t', '--template', type=str, help='Template for generating passwords.')
    parser.add_argument('-c', '--count', type=int, default=DEFAULT_COUNT, help='Number of passwords to generate.')
    parser.add_argument('-v', '--verbose', action='count', default=LOG_LEVEL_INFO, help='Set the verbosity level of logging.')
    parser.add_argument('-f', '--file', type=str, help='Path to a file containing password patterns.')
    parser.add_argument('-r', '--randomize', action='store_true', help='Randomly permute characters of the password.')

    args, unknown = parser.parse_known_args()

    if unknown:
        print(f"Unknown arguments: {unknown}. Use '--help' for help.")
        sys.exit(1)

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
        sys.exit(1)

def process_password_file(args, pm, general_logger, debug_logger):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', args.file)
    try:
        with open(file_path, 'r') as file:
            patterns = file.read().splitlines()
            for pattern in patterns:
                if pattern.strip():
                    for _ in range(args.count):
                        password = pm.generate_pattern_password(pattern.strip())
                        general_logger.info(f"Generated password from pattern: {pattern.strip()}")
                        debug_logger.debug(f"Pattern used: {pattern.strip()}, Generated password: {password}")
                        print(password)
    except FileNotFoundError:
        general_logger.error(f"File not found: {file_path}")
        print(f"File not found: {file_path}")
        sys.exit(1)

def generate_from_template(args, pm, general_logger, debug_logger):
    passwords = []
    for _ in range(args.count):
        password = pm.generate_pattern_password(args.template)
        general_logger.info(f"Generated password from template: {args.template}")
        debug_logger.debug(f"Template used: {args.template}, Generated password: {password}")
        passwords.append(password)
    return passwords

def generate_random_passwords(args, pm, general_logger, debug_logger):
    for _ in range(args.count):
        password = pm.generate_random_password(args.length, args.charset)
        general_logger.info("Generated random password.")
        debug_logger.debug(f"Charset used: {args.charset}, Generated password: {password}")
        print(password)

if __name__ == '__main__':
    main()
