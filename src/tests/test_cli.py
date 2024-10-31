import unittest
from unittest.mock import patch
from io import StringIO
from src.cli.main import main


class TestCLI(unittest.TestCase):
    @patch("sys.argv", ["main.py", "* * * * * /usr/bin/find"])
    def test_main(self) -> None:
        """
        Tests that the main function prints the expected output when given a valid cron string.

        The output should include the fields "minute", "hour", "day of month", "month", "day of week", and "command".
        """
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            main()
            self.assertIn("minute", fake_stdout.getvalue())
            self.assertIn("hour", fake_stdout.getvalue())
            self.assertIn("day of month", fake_stdout.getvalue())
            self.assertIn("month", fake_stdout.getvalue())
            self.assertIn("day of week", fake_stdout.getvalue())
            self.assertIn("command", fake_stdout.getvalue())

    @patch("sys.argv", ["main.py", "invalid * * * * /usr/bin/find"])
    def test_main_invalid_cron_string(self) -> None:
        """
        Tests that the main function exits the program with an error when given an invalid cron string.

        The error message should include the text "Invalid field value: invalid".
        """
        with patch("sys.stderr", new=StringIO()) as fake_stderr:
            with self.assertRaises(SystemExit):
                main()
            self.assertIn("Invalid field value: invalid", fake_stderr.getvalue())

    @patch("sys.argv", ["main.py"])
    def test_main_missing_cron_string(self) -> None:
        """
        Test that the main function exits the program with an error when the cron string argument is missing.

        The error message should indicate that the argument 'cron_string' is required.
        """
        with patch("sys.stderr", new=StringIO()) as fake_stderr:
            with self.assertRaises(SystemExit):
                main()
            self.assertIn(
                "the following arguments are required: cron_string",
                fake_stderr.getvalue(),
            )


if __name__ == "__main__":
    unittest.main()
