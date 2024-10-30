import sys
from typing import Dict, List
from datetime import datetime


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
            self.fields = self.parse_fields()
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    def parse_fields(self) -> Dict[str, List[str]]:
        """
        Parses the cron string into a dictionary of fields.

        The dictionary contains the fields "minute", "hour", "day of month", "month",
        "day of week", and "command". Each field is a list of strings, where each string
        is a value for the corresponding field.

        If the cron string is invalid, a ValueError is raised.
        """
        fields = self.cron_string.split()
        if len(fields) != 6:
            raise ValueError("Invalid cron string")

        return {
            "minute": self.parse_field(fields[0], 0, 59),
            "hour": self.parse_field(fields[1], 0, 23),
            "day_of_month": self.parse_field(fields[2], 1, 31),
            "month": self.parse_field(fields[3], 1, 12),
            "day_of_week": self.parse_field(fields[4], 0, 6),
            "command": fields[5],
        }

    def parse_field(self, field: str, min_value: int, max_value: int) -> List[str]:
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
            return [value for value in values if min_value <= int(value) <= max_value]

        try:
            value = int(field)
            if value < min_value or value > max_value:
                raise ValueError
            return [field]
        except ValueError:
            raise ValueError(f"Invalid field value: {field}")

    def get_expanded_fields(self) -> Dict[str, List[str]]:
        """
        Retrieves the expanded fields from the parsed cron string.

        Returns:
            Dict[str, List[str]]: A dictionary containing the expanded fields where each key represents a field
            (e.g., "minute", "hour") and the corresponding value is a list of strings representing the values of that field.
        """
        return self.fields
    
    def find_next_n_occurrences(self, n: int) -> List[str]:
        """
        Finds the next n occurrences of the cron job.

        Args:
            n (int): The number of occurrences to find.

        Returns:
            List[str]: A list of the next n occurrences in the format YYYY-MM-DD HH:MM.
        """

        current_time = datetime.now()
        current_year = current_time.year
        next_occurrences = []

        month_list = [int(month) for month in self.fields["month"]]
        day_of_month_list = [int(day) for day in self.fields["day_of_month"]]

        while len(next_occurrences) < n:
            for month in month_list:
                if current_time.year == current_year and current_time.month < month:
                    continue
                for day_of_month in day_of_month_list:
                    for hour in self.fields["hour"]:
                        for minute in self.fields["minute"]:
                            try:
                                next_time = datetime(current_year, month, day_of_month, int(hour), int(minute))
                                if current_time <= next_time and next_time.weekday() + 1 in set(int(day) for day in self.fields["day_of_week"]):
                                    next_occurrences.append(next_time.strftime('%Y-%m-%d %H:%M'))
                                    if len(next_occurrences) == n:
                                        return next_occurrences
                            except ValueError:
                                continue
            current_year += 1
        return next_occurrences
