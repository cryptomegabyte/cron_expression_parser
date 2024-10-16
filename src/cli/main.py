import argparse
import sys
from tabulate import tabulate
from src.cron_parser.parser import CronParser


def main():
    try:
        parser = argparse.ArgumentParser(description="Cron Expression Parser")
        parser.add_argument("cron_string", help="Cron string to parse")
        args = parser.parse_args()

        cron_parser = CronParser(args.cron_string)
        expanded_fields = cron_parser.get_expanded_fields()

        table = [
            ["Field", "Values"],
            ["minute", ", ".join(expanded_fields["minute"])],
            ["hour", ", ".join(expanded_fields["hour"])],
            ["day of month", ", ".join(expanded_fields["day_of_month"])],
            ["month", ", ".join(expanded_fields["month"])],
            ["day of week", ", ".join(expanded_fields["day_of_week"])],
            ["command", expanded_fields["command"]],
        ]

        print(tabulate(table, headers="firstrow", tablefmt="grid"))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
