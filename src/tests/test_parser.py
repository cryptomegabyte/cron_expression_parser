import unittest
from src.cron_parser.parser import CronParser

class TestCronParser(unittest.TestCase):
    def test_parse_fields(self):
        cron_string = "* * * * * /usr/bin/find"
        cron_parser = CronParser(cron_string)
        expanded_fields = cron_parser.get_expanded_fields()

        self.assertEqual(expanded_fields["minute"], [str(i) for i in range(60)])
        self.assertEqual(expanded_fields["hour"], [str(i) for i in range(24)])
        self.assertEqual(expanded_fields["day_of_month"], [str(i) for i in range(1, 32)])
        self.assertEqual(expanded_fields["month"], [str(i) for i in range(1, 13)])
        self.assertEqual(expanded_fields["day_of_week"], [str(i) for i in range(7)])
        self.assertEqual(expanded_fields["command"], "/usr/bin/find")

    def test_parse_field_with_step(self):
        cron_string = "*/15 * * * * /usr/bin/find"
        cron_parser = CronParser(cron_string)
        expanded_fields = cron_parser.get_expanded_fields()

        self.assertEqual(expanded_fields["minute"], [str(i) for i in range(0, 60, 15)])

    def test_parse_field_with_range(self):
        cron_string = "1-5 * * * * /usr/bin/find"
        cron_parser = CronParser(cron_string)
        expanded_fields = cron_parser.get_expanded_fields()

        self.assertEqual(expanded_fields["minute"], [str(i) for i in range(1, 6)])

    def test_parse_field_with_list(self):
        cron_string = "1,3,5 * * * * /usr/bin/find"
        cron_parser = CronParser(cron_string)
        expanded_fields = cron_parser.get_expanded_fields()

        self.assertEqual(expanded_fields["minute"], ["1", "3", "5"])

    def test_parse_field_with_single_value(self):
        cron_string = "1 * * * * /usr/bin/find"
        cron_parser = CronParser(cron_string)
        expanded_fields = cron_parser.get_expanded_fields()

        self.assertEqual(expanded_fields["minute"], ["1"])

    def test_invalid_cron_string(self):
        cron_string = "invalid * * * * /usr/bin/find"
        with self.assertRaises(SystemExit):
            CronParser(cron_string)

if __name__ == "__main__":
    unittest.main()