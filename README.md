# Cron Expression Parser
=========================

A command-line application that parses a cron string and expands each field to show the times at which it will run.

## Overview

This application takes a cron string as input and outputs a table showing the times at which the cron job will run. It supports the standard cron format with five time fields (minute, hour, day of month, month, and day of week) plus a command.

## Installation

To install the application, run the following command:
```bash
pip install -r requirements.txt
```

## Usage

To run the application, use the following command:

```bash
python src/cli/main.py <cron_string>
```

## Example

Here's an example usage of the application:

```bash
python src/cli/main.py "*/15 0 1,15 * 1-5 /usr/bin/find"
```

This will ouput the following table:

```bash

minute  0 15 30 45
hour    0
day of month  1 15
month  1 2 3 4 5 6 7 8 9 10 11 12
day of week  1 2 3 4 5
command  /usr/bin/find

```

## Development

To contribute to the development of this application, please fork this repository and submit a pull request with your changes.

## Testing

To run the tests, use the following command:

```bash
python -m unittest discover -s src/tests
```

### License

This application is licensed under the [MIT License][1].

### Authors

Ali Kayani

[1]: https://opensource.org/license/mit