from setuptools import setup, find_packages

setup(
    name='passwordGenerator',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'argparse==1.4.0'
    ],
    entry_points={
        'console_scripts': [
            'password-generator=cli.main:main',
        ],
    },
)
