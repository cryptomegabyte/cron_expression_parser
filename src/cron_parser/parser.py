import sys
from typing import Dict, List


class CronParser:
    def __init__(self, cron_string: str) -> None:
        """
        Initializes the CronParser with a cron string.

        The cron string should be a string consisting of five space-separated fields:
        minute, hour, day of month, month, and day of week. The string should also
        include a command as the sixth field.

        If the cron string is invalid, a ValueError is raised.
        """
        try:
            self.cron_string = cron_string
            self.month_names = {
                "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
                "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12
            }

            self.day_names = {
                "sun": 0, "mon": 1, "tue": 2, "wed": 3, "thu": 4, "fri": 5, "sat": 6
            }

            self.fields = self.parse_fields()
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    def parse_fields(self):
        fields = self.cron_string.split()
        if len(fields) != 6:
            raise ValueError("Invalid cron string")

        return {
            "minute": self.parse_field(fields[0], 0, 59),
            "hour": self.parse_field(fields[1], 0, 23),
            "day_of_month": self.parse_field(fields[2], 1, 31),
            "month": self.parse_field(fields[3], 1, 12, "month"),
            "day_of_week": self.parse_field(fields[4], 0, 6, "day_of_week"),
            "command": fields[5],
        }
    def parse_field(self, field: str, min_value: int, max_value: int, field_name: str = None) -> List[str]:
        """
        Parses a field in the cron string.

        The field should be a string consisting of one of the following formats:

        - "*": All values in the range [min_value, max_value]
        - "*/step": Every step value in the range [min_value, max_value], starting from min_value
        - "value/step": Every step value in the range [value, max_value], starting from value
        - "start-end": The range of values [start, end]
        - "value1,value2,...": The specific values value1, value2, ...

        If the field is invalid, a ValueError is raised.

        Args:
            field (str): The field to parse.
            min_value (int): The minimum value of the range.
            max_value (int): The maximum value of the range.
            field_name (str): The name of the field (e.g. "month", "day_of_week").

        Returns:
            List[str]: A list of strings, where each string is a value for the corresponding field.
        """
        if field == "*":
            return [str(i) for i in range(min_value, max_value + 1)]

        if "/" in field:
            if field.startswith("*"):
                _, step = field.split("/")
                step = int(step)
                return [str(i) for i in range(min_value, max_value + 1, step)]
            else:
                value, step = field.split("/")
                value = int(value)
                step = int(step)
                return [str(i) for i in range(value, max_value + 1, step)]

        if "-" in field:
            start, end = field.split("-")
            start = int(start)
            end = int(end)
            return [str(i) for i in range(start, end + 1)]

        if "," in field:
            values = field.split(",")
            if field_name == "day_of_week":
                return [str(self.day_names[value]) for value in values if value in self.day_names]
            else:
                return [value for value in values if min_value <= int(value) <= max_value]
        elif field_name == "day_of_week" and field in self.day_names:
            return [str(self.day_names[field])]

        if field_name == "month":
            if field in self.month_names:
                return [str(self.month_names[field])]
            else:
                raise ValueError(f"Invalid month name: {field}")

        try:
            value = int(field)
            if value < min_value or value > max_value:
                raise ValueError
            return [field]
        except ValueError:
            raise ValueError(f"Invalid value for field: {field}")

    def get_expanded_fields(self) -> Dict[str, List[str]]:
        """
        Retrieves the expanded fields from the parsed cron string.

        Returns:
            Dict[str, List[str]]: A dictionary containing the expanded fields where each key represents a field
            (e.g., "minute", "hour") and the corresponding value is a list of strings representing the values of that field.
        """
        return self.fields
