import sys
from typing import Dict, List


class CronParser:
    def __init__(self, cron_string: str):
        try:
            self.cron_string = cron_string
            self.fields = self.parse_fields()
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    def parse_fields(self) -> Dict[str, List[str]]:
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
        return self.fields
