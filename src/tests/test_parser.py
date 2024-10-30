import unittest
from src.cron_parser.parser import CronParser


class TestCronParser(unittest.TestCase):
    def test_parse_fields(self) -> None:
        """
        Tests that the fields are parsed correctly when they are all wildcarded (*).

        The expanded fields should be a list of strings, where each string is a value
        for the corresponding field. The values should be in increasing order.

        For example, the minute field should be a list of strings "0" through "59", and
        the day of week field should be a list of strings "0" through "6".
        """
        cron_string = "* * * * * /usr/bin/find"
        cron_parser = CronParser(cron_string)
        expanded_fields = cron_parser.get_expanded_fields()

        self.assertEqual(expanded_fields["minute"], [str(i) for i in range(60)])
        self.assertEqual(expanded_fields["hour"], [str(i) for i in range(24)])
        self.assertEqual(
            expanded_fields["day_of_month"], [str(i) for i in range(1, 32)]
        )
        self.assertEqual(expanded_fields["month"], [str(i) for i in range(1, 13)])
        self.assertEqual(expanded_fields["day_of_week"], [str(i) for i in range(7)])
        self.assertEqual(expanded_fields["command"], "/usr/bin/find")

    def test_parse_field_with_step(self) -> None:
        """
        Tests that a field with a step value (e.g. "*/15") is parsed correctly.

        The expanded field should be a list of strings, where each string is a value
        for the corresponding field. The values should be in increasing order, and
        should be spaced by the given step value.

        For example, the minute field should be a list of strings "0", "15", "30", and
        "45".
        """
        cron_string = "*/15 * * * * /usr/bin/find"
        cron_parser = CronParser(cron_string)
        expanded_fields = cron_parser.get_expanded_fields()

        self.assertEqual(expanded_fields["minute"], [str(i) for i in range(0, 60, 15)])

    def test_parse_field_with_range(self) -> None:
        """
        Tests that a field with a range (e.g. "1-5") is parsed correctly.

        The expanded field should be a list of strings, where each string is a value
        for the corresponding field. The values should be in increasing order, and
        should be within the given range.

        For example, the minute field should be a list of strings "1", "2", "3", "4", and
        "5".
        """
        cron_string = "1-5 * * * * /usr/bin/find"
        cron_parser = CronParser(cron_string)
        expanded_fields = cron_parser.get_expanded_fields()

        self.assertEqual(expanded_fields["minute"], [str(i) for i in range(1, 6)])

    def test_parse_field_with_list(self) -> None:
        """
        Tests that a field with a list of values (e.g. "1,3,5") is parsed correctly.

        The expanded field should be a list of strings, where each string is a value
        for the corresponding field. The values should be in increasing order, and
        should be within the given list.

        For example, the minute field should be a list of strings "1", "3", and "5".
        """
        cron_string = "1,3,5 * * * * /usr/bin/find"
        cron_parser = CronParser(cron_string)
        expanded_fields = cron_parser.get_expanded_fields()

        self.assertEqual(expanded_fields["minute"], ["1", "3", "5"])

    def test_parse_field_with_single_value(self) -> None:
        """
        Tests that a field with a single value (e.g. "1") is parsed correctly.

        The expanded field should be a list of strings, where each string is a value
        for the corresponding field. The values should be in increasing order, and
        should be within the given value.

        For example, the minute field should be a list of strings "1".
        """
        cron_string = "1 * * * * /usr/bin/find"
        cron_parser = CronParser(cron_string)
        expanded_fields = cron_parser.get_expanded_fields()

        self.assertEqual(expanded_fields["minute"], ["1"])

    def test_invalid_cron_string(self) -> None:
        """
        Tests that an invalid cron string raises a SystemExit exception.

        This ensures that when the cron string contains invalid field values,
        the CronParser exits the program with an error.
        """
        cron_string = "invalid * * * * /usr/bin/find"
        with self.assertRaises(SystemExit):
            CronParser(cron_string)

    def test_find_next_n_occurrences(self) -> None:
        """
        Tests that the find_next_n_occurrences method returns the correct number of occurrences.
        """
        cron_string = "*/15 0 1,15 * 1-5 /usr/bin/find"
        cron_parser = CronParser(cron_string)
        next_occurrences = cron_parser.find_next_n_occurrences(5)
        self.assertEqual(len(next_occurrences), 5)

        next_occurrences = cron_parser.find_next_n_occurrences(10)
        self.assertEqual(len(next_occurrences), 10)


if __name__ == "__main__":
    unittest.main()
