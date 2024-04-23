import argparse
import sys
import string
from password_gen import generate_random_password, generate_pattern_password
from modules.logger import setup_logger
# Добавим путь к корневому каталогу проекта для импорта password_gen
# sys.path.insert(0, '..')

def main():
    parser = argparse.ArgumentParser(description="Password Generator Tool")
    parser.add_argument('-n', '--length', type=int, default=8, help='Length of the password')
    parser.add_argument('-S', '--charset', type=str, default=string.ascii_letters + string.digits,
                        help='Character set from which to generate the password')
    parser.add_argument('-t', '--template', type=str, help='Template for generating passwords using a specific pattern')
    parser.add_argument('-vvv', '--verbose', action='store_true', help='Enable verbose output')

    args = parser.parse_args()
    setup_logger(args.verbose)

    if args.template:
        password = generate_pattern_password(args.template)
    else:
        password = generate_random_password(args.length, args.charset)

    print(f"Generated Password: {password}")


if __name__ == "__main__":
    main()
