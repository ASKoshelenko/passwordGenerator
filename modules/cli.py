import argparse
import string
import logging
import os
from passwordGenerator.password_gen.random_password import generate_random_password
from passwordGenerator.password_gen.pattern_password import generate_pattern_password
from passwordGenerator.modules.logger import setup_logging

def main():
    epilog = """
    Password Generator Tool is a versatile command-line utility designed for generating secure passwords based on specified parameters. It can operate in several modes, handling both random and pattern-based password generation.

    Examples:
      Generate a random 16-character password:
        python -m passwordGenerator.modules.cli -n 16

      Generate a password using a specific character set:
        python -m passwordGenerator.modules.cli -S abc123 -n 10

      Generate a password based on a pattern:
        python -m passwordGenerator.modules.cli -t "u{4}d{3}\\-l{2}"

      Write generated password to a log file with detailed debug information:
        python -m passwordGenerator.modules.cli -vvv -w

      Generate passwords from a file of patterns, each pattern 3 times:
        python -m passwordGenerator.modules.cli -f patterns.txt -c 3

      Display this help message and exit:
        python -m passwordGenerator.modules.cli -h
    """

    parser = argparse.ArgumentParser(
        description="Password Generator Tool",
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('-n', '--length', type=int, default=12, help='Specifies the length of the password. Default is 12.')
    parser.add_argument('-S', '--charset', type=str, default=None, help='Specifies the character set used for the password. Default is alphanumeric.')
    parser.add_argument('-t', '--template', type=str, help='Specifies a template for generating passwords according to a pattern.')
    parser.add_argument('-v', '--verbose', action='count', default=0, help='Increases verbosity level. Use multiple times for more detail (e.g., -vvv).')
    parser.add_argument('-w', '--write', action='store_true', help='Writes the output to a file named "logs.txt".')
    parser.add_argument('-f', '--file', type=str, help='File with list of password patterns.')
    parser.add_argument('-c', '--count', type=int, default=1, help='Number of passwords to generate for each pattern.')

    args = parser.parse_args()
    logger = setup_logging(args.verbose, args.write)  # Получаем настроенный логгер

    if args.file:
        try:
            with open(args.file, 'r') as file:
                patterns = file.readlines()
                for pattern in patterns:
                    pattern = pattern.strip().replace(' ', '')  # Удаление пробелов
                    for _ in range(args.count):
                        password = generate_pattern_password(pattern)
                        logger.info(f"Generated password from file pattern '{pattern}': {password}")
                        if args.verbose > 0:
                            logger.debug(f"Password pattern used: {pattern}")
                        print(f"Generated Password from pattern '{pattern}': {password}")
        except FileNotFoundError:
            print(f"Error: The file {args.file} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")
    elif args.template:
        password = generate_pattern_password(args.template)
        logger.info(f"Generated password from template '{args.template}': {password}")
        if args.verbose > 0:
            logger.debug(f"Template used: {args.template}")
    else:
        charset = args.charset if args.charset else string.ascii_letters + string.digits
        password = generate_random_password(args.length, charset)
        logger.info(f"Generated random password using charset '{charset}': {password}")
        if args.verbose > 0:
            logger.debug("Password generated successfully")
        if args.verbose > 1:
            logger.debug(f"Charset used for generation: {charset}")
            logger.debug(f"Password length: {args.length}")

    print(f"Generated Password: {password}")

if __name__ == '__main__':
    main()
