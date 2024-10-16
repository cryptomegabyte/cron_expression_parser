# Usage
================

The cron expression parser is a command-line tool that takes a cron string as input and outputs the expanded fields.

## Command-Line Options
------------------------

The cron expression parser has the following command-line options:

* `cron_string`: The cron string to parse.

## Example Usage
----------------

To parse a cron string, simply run the command with the cron string as an argument:

```bash
$ cron-expression-parser "* * * * * /usr/bin/find"
```
```bash
+---------------+---------------------------------------+
| Field         | Values                                |
+===============+=======================================+
| minute        | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ... |
| hour          | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ... |
| day of month  | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...    |
| month         | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...    |
| day of week   | 0, 1, 2, 3, 4, 5, 6                   |
| command       | /usr/bin/find                         |
+---------------+---------------------------------------+
```

Cron String Format
The cron string format is as follows:

```bash
minute hour day_of_month month day_of_week command
```

Where:

`minute`: The minute of the hour (0-59)
`hour`: The hour of the day (0-23)
`day_of_month`: The day of the month (1-31)
`month`: The month of the year (1-12)
`day_of_week`: The day of the week (0-6)
`command`: The command to run

You can use the following special characters in the cron string:

`*`: Matches all values
`/`: Specifies a step value
`-`: Specifies a range of values
`,`: Specifies a list of values

For example:

```bash
*/15 * * * * /usr/bin/find  # Run every 15 minutes
1-5 * * * * /usr/bin/find  # Run at 1, 2, 3, 4, and 5 minutes past the hour
1,3,5 * * * * /usr/bin/find  # Run at 1, 3, and 5 minutes past the hour
```

Note that the cron string format is case-sensitive.

