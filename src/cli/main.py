import argparse
import sys
import logging
from tabulate import tabulate
from src.cron_parser.parser import CronParser


def main() -> None:
    """
    Main function for the command-line interface.

    This function parses the command-line arguments and passes the cron string to
    the CronParser. It then prints the expanded fields as a table.
    """
    try:
        parser = argparse.ArgumentParser(description="Cron Expression Parser")
        parser.add_argument("cron_string", help="Cron string to parse")
        parser.add_argument("-l", "--log", action="store_true", help="Enable logging")
        args = parser.parse_args()

        if args.log:
            logging.basicConfig(
                level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
            )

        logging.info(f"Parsing cron string: {args.cron_string}")

        cron_parser = CronParser(args.cron_string)
        expanded_fields = cron_parser.get_expanded_fields()

        if args.log:
            logging.info("Expanded fields:")
            logging.info(expanded_fields)

        table = [
            ["Field", "Values"],
            ["minute", ", ".join(expanded_fields["minute"])],
            ["hour", ", ".join(expanded_fields["hour"])],
            ["day of month", ", ".join(expanded_fields["day_of_month"])],
            ["month", ", ".join(expanded_fields["month"])],
            ["day of week", ", ".join(expanded_fields["day_of_week"])],
            ["command", expanded_fields["command"]],
        ]

        if args.log:
            logging.info("Printing expanded fields as table:")
        print(tabulate(table, headers="firstrow", tablefmt="grid"))
    except Exception as e:
        if args.log:
            logging.error(f"Error: {e}")
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
