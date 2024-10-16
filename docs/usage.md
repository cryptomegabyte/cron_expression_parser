# Usage
================

The cron expression parser is a command-line tool that takes a cron string as input and outputs the expanded fields.

## Command-Line Options
The cron expression parser has the following command-line options:

`cron_string`: The cron string to parse.

## Example Usage
To parse a cron string, simply run the command with the cron string as an argument:

```bash
make run
```

This will run the program with a default cron string. To specify a custom cron string, you can use the following command:

```bash
python -m src.cli.main "<cron_string>"
```

## Running Tests
To run the tests, use the following command:

```bash
make test
```

Cleaning Up
To remove any temporary files, use the following command:

```bash
make clean
```

## Generating Documentation
To generate documentation, use the following command:

```bash
make docs
```

Cron String Format The cron string format is as follows:

```bash
minute hour day_of_month month day_of_week command
```

Where:

- `minute`: The minute of the hour (0-59)
- `hour`: The hour of the day (0-23)
- `day_of_month`: The day of the month (1-31)
- `month`: The month of the year (1-12)
- `day_of_week`: The day of the week (0-6)
- `command`: The command to run