import argparse
import string

from passwordGenerator.password_gen.random_password import generate_random_password
from passwordGenerator.password_gen.pattern_password import generate_pattern_password
from passwordGenerator.modules.logger import setup_logging

def main():
    parser = argparse.ArgumentParser(description="Password Generator Tool")
    parser.add_argument('-n', '--length', type=int, default=12, help='Length of the password')
    parser.add_argument('-S', '--charset', type=str, default=None, help='Character set for the password')
    parser.add_argument('-t', '--template', type=str, help='Password pattern template')
    parser.add_argument('-v', '--verbose', action='count', default=0, help='Verbose output, increment for more verbosity')
    parser.add_argument('-w', '--write', action='store_true', help='Write output to file')

    args = parser.parse_args()
    setup_logging(args.verbose, args.write)

    if args.template:
        password = generate_pattern_password(args.template)
    else:
        charset = args.charset if args.charset else string.ascii_letters + string.digits
        password = generate_random_password(args.length, charset)

    print(f"Generated Password: {password}")

if __name__ == '__main__':
    main()
