# Cron Expression Parser
=========================

A command-line application that parses a cron string and expands each field to show the times at which it will run.

## Overview

This application takes a cron string as input and outputs a table showing the times at which the cron job will run. It supports the standard cron format with five time fields (minute, hour, day of month, month, and day of week) plus a command.

## Installation

Create a Virtual Environment
Before installing the requirements, it's recommended to create a virtual environment to isolate the dependencies of this project. Here's how to create a virtual environment using python -m venv:

```bash
python -m venv venv
```

This will create a new virtual environment in a directory named `venv`.

## Activate the Virtual Environment

To activate the virtual environment, run the following command:

```bash
source venv/bin/activate
```

On Windows, use the following command instead:

```bash
venv\Scripts\activate
```

## Install Requirements

Once the virtual environment is activated, you can install the requirements using the following command:

```bash
pip install -r requirements.txt
```

## Usage
See [usage.md][1] for instructions on how to use the application.

## Development
To contribute to the development of this application, please fork this repository and submit a pull request with your changes.

## Testing
To run the tests, use the following command:

```bash
make test
```

By adding this section, we can help users set up a virtual environment and avoid potential issues with dependency conflicts.

[1]: docs/usage.md