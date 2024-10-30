import argparse
import sys
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
        parser.add_argument("-n", "--num-occurrences", type=int, nargs="?", const=1, help="Number of occurrences to predict (optional)")
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

        if args.num_occurrences is not None:
            next_occurrences = cron_parser.find_next_n_occurrences(args.num_occurrences)
            next_occurrences_table = [["Occurrence", "Date and Time"]]
            for i, occurrence in enumerate(next_occurrences, start=1):
                next_occurrences_table.append([i, occurrence])
            print(tabulate(next_occurrences_table, headers="firstrow", tablefmt="grid"))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
