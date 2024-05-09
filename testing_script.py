import subprocess

def run_command(command):
    """Запускает команду в системе и возвращает вывод."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        return stdout.decode('utf-8').strip()
    else:
        return f"Error: {stderr.decode('utf-8').strip()}"

def main():
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
        "python -m cli.main -n 8 -S 'abc123!@#' -c 5",  # Генерация простых паролей с кастомным набором символов
        "python -m cli.main -f '../data/password_patterns.txt' -c 2 -vv"  # Чтение шаблонов из файла и генерация с повышенной подробностью логирования
    ]

    for cmd in commands:
        result = run_command(cmd)
        print(f"Command: {cmd}\nResult: \n{result}\n")


if __name__ == '__main__':
    main()
