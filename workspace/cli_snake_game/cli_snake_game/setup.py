from setuptools import setup, find_packages

setup(
    name='cli_snake_game',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cli_snake_game = main:main',
        ],
    },
    install_requires=[
        'curses==2.2',
        'random==1.2.1',
        'time==1.7',
        'json==2.0.9',
        'argparse==1.1',
        'unittest==1.0.1',
        'setuptools==57.4.0',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A command-line interface snake game',
)
