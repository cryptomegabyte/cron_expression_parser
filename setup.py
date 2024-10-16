import os
from setuptools import setup, find_packages

# Get the version number from the __version__ variable in version.py
with open('version.py') as f:
    exec(f.read())

# Get the long description from the README file
with open('README.md', 'r') as f:
    long_description = f.read()

# Define the setup configuration
setup(
    name='cron-expression-parser',
    version=__version__,
    description='A command-line application that parses a cron string and expands each field to show the times at which it will run.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/your-username/cron-expression-parser',
    author='Your Name',
    author_email='your-email@example.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'argparse==1.4.0',
        'tabulate==0.8.9',
    ],
    entry_points={
        'console_scripts': [
            'cron-expression-parser=src.cli.main:main',
        ],
    },
    test_suite='tests',
    tests_require=[
        'unittest>=3.2',
        'pytest>=6.2.2',
    ],
)