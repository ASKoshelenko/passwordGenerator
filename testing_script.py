import subprocess

def run_command(command):
    """
    Executes a shell command and returns its output or an error message.

    Args:
        command (str): The command string to execute in the shell.

    Returns:
        str: The standard output from the command if successful, or an error message if the command fails.
    """
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        return stdout.decode('utf-8').strip()
    else:
        return f"Error: {stderr.decode('utf-8').strip()}"

def main():
    """
    Main function to execute a series of predefined CLI commands for a password generator application.
    Each command is designed to test different functionalities of the password generator.

    The output of each command is printed, providing a clear view of its execution result.
    """
    commands = [
        "python -m cli.main -t 'a{10}' -c 1",
        "python -m cli.main -t 'A{10}' -c 1",
        "python -m cli.main -t 'U{10}' -c 1",
        "python -m cli.main -t 'h{10}' -c 1",
        "python -m cli.main -t 'H{10}' -c 1",
        "python -m cli.main -t 'v{10}' -c 1",
        "python -m cli.main -t 'V{10}' -c 1",
        "python -m cli.main -t 'Z{10}' -c 1",
        "python -m cli.main -t 'c{10}' -c 1",
        "python -m cli.main -t 'C{10}' -c 1",
        "python -m cli.main -t 'z{10}' -c 1",
        "python -m cli.main -t 'b{10}' -c 1",
        "python -m cli.main -t 's{10}' -c 1",
        "python -m cli.main -t 'S{10}' -c 1",
        "python -m cli.main -t 'x{10}' -c 1",
        "python -m cli.main -t 'H{10}' -r -c 1",
        "python -m cli.main -t 'H{32}' -r -c 1",
        "python -m cli.main -t 'H{64}' -r -c 1",
        "python -m cli.main -t 'HH-HH-HH-HH-HH-HH' -c 3",
        "python -m cli.main -t 'uullA{6}' -r -c 1",
        "python -m cli.main -t '@[ABCDEF]{9}' -r -c 1",
        "python -m cli.main -n 8 -S 'abc123!@#' -c 5",
        "python -m cli.main -n 10 -S 'abcABC123' -c 5",
        "python -m cli.main -t 'u{4}d{3}l{2}' -c 2 -vvv",
        "python -m cli.main -f '../data/password_patterns.txt' -c 2 -vv",
        "python -m cli.main -t 'L{10}' -r -c 1",
        "python -m cli.main -t '[dpl]{5}' -c 3",
        "python -m cli.main -t 'ddddd' -c 5",
        "python -m cli.main -t 'u{4}d{3}-l{2}' -c 1",
        "python -m cli.main -t 'u{4}[dl]{3}-l{2}' -c 1",
        "python -m cli.main -t '[d|l]{10}'",
    ]

    for cmd in commands:
        result = run_command(cmd)
        print(f"Command: {cmd}\nResult: \n{result}\n")


if __name__ == '__main__':
    main()
