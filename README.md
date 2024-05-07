# Password Generator

## Description

Password Generator is a versatile command-line utility designed for generating secure passwords based on specified parameters. It can operate in several modes, handling both random and pattern-based password generation.

## Features

- Generate passwords with specified length and character sets.
- Generate passwords based on pre-defined patterns.
- Capability to generate multiple passwords at once.
- Detailed logging of password generation with adjustable verbosity.
- Write password generation results to a log file.

## Installation

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/ASKoshelenko/PasswordGenerator.git
cd PasswordGenerator
```

## Install the necessary packages:
```bash
pip install -r requirements.txt
```
or
```bash
python setup.py install 
```
## Usage

Generate a Random Password
To generate a random 16-character password:

```bash
python -m cli.main -n 16
```

## Generate a Password with a Specific Character Set
To generate a password using a specific set of characters (e.g., abc123), specify the length and character set:
```
bash
python -m cli.main -S abc123 -n 10 -c 5
```
## Generate a Password from a Pattern
To generate a password based on a pattern (e.g., "4 uppercase letters followed by 3 digits and 2 lowercase letters"):
```bash
python -m cli.main -t "u{4}d{3}\\-l{2}"
```

## Write Generated Password to a Log File
For verbose output and writing the generation process and result to a log file:
```bash
python -m cli.main -vvv -w
```

## Generate Passwords from a File of Patterns
To generate passwords from a list of patterns stored in a file, specify the file path and the number of times each pattern should be used:
```bash
python -m cli.main -f patterns.txt -c 3
```

## Display Help
For a detailed description of all commands and options:

```bash
python -m cli.main -h
```

## Configuration
The logging behavior can be adjusted in the config/logger.py file. Default settings write logs to logs.txt in the logs directory.

## Contributing
Contributions are welcome. Please fork the repository and submit a pull request with your enhancements.

## License
Specify your project's license here, e.g., MIT, GPL, etc.

This README provides a comprehensive guide to installing, configuring, and using the Password Generator tool, aligning with the updated structure and capabilities of your application. Adjust the paths and URLs as per your repository details.
DM
