import argparse
import string
from passwordGenerator.password_gen.password_manager import PasswordManager
from passwordGenerator.config.logger import setup_logging

def main():
    parser = argparse.ArgumentParser(description="Password Generator Tool")
    parser.add_argument('-n', '--length', type=int, default=12, help='Specifies the length of the password.')
    parser.add_argument('-S', '--charset', type=str, default=string.ascii_letters + string.digits, help='Character set for the password.')
    parser.add_argument('-t', '--template', type=str, help='Specifies a template for generating passwords.')
    parser.add_argument('-c', '--count', type=int, default=1, help='Number of passwords to generate.')
    parser.add_argument('-v', '--verbose', action='count', default=0, help='Increases verbosity level.')
    parser.add_argument('-f', '--file', type=str, help='File with list of password patterns.')

    args, unknown = parser.parse_known_args()  # Catch unknown args
    if unknown:
        print(f"Unknown arguments: {unknown}")
        return

    logger, debug_logger = setup_logging(args.verbose)

    pm = PasswordManager()

    try:
        if args.template:
            for _ in range(args.count):
                password = pm.generate_pattern_password(args.template)
                logger.info(f"Generated password from template: {args.template}")
                if debug_logger:
                    debug_logger.debug(f"Template used: {args.template}, Password: {password}")
                print(password)
        else:
            for _ in range(args.count):
                password = pm.generate_random_password(args.length, args.charset)
                logger.info("Generated random password.")
                if debug_logger:
                    debug_logger.debug(f"Charset used: {args.charset}, Password: {password}")
                print(password)
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        if debug_logger:
            debug_logger.error(f"Exception details: {str(e)}")

if __name__ == '__main__':
    main()
