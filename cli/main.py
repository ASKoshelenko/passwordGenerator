import argparse
import string
import logging

from password_gen.random_password import generate_random_password
from password_gen.pattern_password import generate_pattern_password
from passwordGenerator.config.logger import setup_logging

def main():
    epilog = """
    Password Generator Tool is a versatile command-line utility designed for generating secure passwords based on specified parameters. It can operate in several modes, handling both random and pattern-based password generation.

    Examples:
      Generate a random 16-character password:
        python -m cli.main -n 16

      Generate a password using a specific character set:
        python -m cli.main -S abc123 -n 10 -c 5

      Generate a password based on a pattern:
        python -m cli.main -t "u{4}d{3}\\-l{2}"

      Write generated password to a log file with detailed debug information:
        python -m cli.main -vvv -w

      Generate passwords from a file of patterns, each pattern 3 times:
        python -m cli.main -f patterns.txt -c 3

      Display this help message and exit:
        python -m cli.main -h
    """

    parser = argparse.ArgumentParser(
        description="Password Generator Tool",
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('-n', '--length', type=int, default=12, help='Specifies the length of the password.')
    parser.add_argument('-S', '--charset', type=str, default=string.ascii_letters + string.digits, help='Character set for the password.')
    parser.add_argument('-t', '--template', type=str, help='Specifies a template for generating passwords according to a pattern.')
    parser.add_argument('-c', '--count', type=int, default=1, help='Number of passwords to generate.')
    parser.add_argument('-v', '--verbose', action='count', default=0, help='Increases verbosity level. Use multiple times for more detail.')
    parser.add_argument('-w', '--write', action='store_true', help='Writes the output to a file named "logs.txt".')
    parser.add_argument('-f', '--file', type=str, help='File with list of password patterns.')

    args = parser.parse_args()
    logger = setup_logging(args.verbose, args.write)  # Setup logger

    if args.file:
        try:
            with open(args.file, 'r') as file:
                patterns = file.readlines()
                for pattern in patterns:
                    pattern = pattern.strip()
                    for _ in range(args.count):
                        password = generate_pattern_password(pattern)
                        logger.info(f"Generated password from file pattern '{pattern}': {password}")
                        print(f"Generated Password from pattern '{pattern}': {password}")
        except FileNotFoundError:
            print(f"Error: The file {args.file} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")
    elif args.template:
        for _ in range(args.count):
            password = generate_pattern_password(args.template)
            logger.info(f"Generated password from template '{args.template}': {password}")
            print(f"Generated Password from template '{args.template}': {password}")
    else:
        for _ in range(args.count):
            password = generate_random_password(args.length, args.charset)
            logger.info(f"Generated random password: {password}")
            print(f"Generated Password: {password}")

if __name__ == '__main__':
    main()
