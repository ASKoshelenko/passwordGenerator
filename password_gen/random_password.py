import random
import string

def generate_random_password(length=12, charset=string.ascii_letters + string.digits):
    """Generate a random password from the specified character set."""
    return ''.join(random.choice(charset) for _ in range(length))
