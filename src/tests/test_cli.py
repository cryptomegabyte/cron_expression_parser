import unittest
from unittest.mock import patch
from io import StringIO
from src.cli.main import main

class TestCLI(unittest.TestCase):
    @patch('sys.argv', ['main.py', '* * * * * /usr/bin/find'])
    def test_main(self):
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            main()
            self.assertIn('minute', fake_stdout.getvalue())
            self.assertIn('hour', fake_stdout.getvalue())
            self.assertIn('day of month', fake_stdout.getvalue())
            self.assertIn('month', fake_stdout.getvalue())
            self.assertIn('day of week', fake_stdout.getvalue())
            self.assertIn('command', fake_stdout.getvalue())

    @patch('sys.argv', ['main.py', 'invalid * * * * /usr/bin/find'])
    def test_main_invalid_cron_string(self):
        with patch('sys.stderr', new=StringIO()) as fake_stderr:
            with self.assertRaises(SystemExit):
                main()
            self.assertIn('Invalid field value: invalid', fake_stderr.getvalue())

    @patch('sys.argv', ['main.py'])
    def test_main_missing_cron_string(self):
        with patch('sys.stderr', new=StringIO()) as fake_stderr:
            with self.assertRaises(SystemExit):
                main()
            self.assertIn('the following arguments are required: cron_string', fake_stderr.getvalue())

if __name__ == "__main__":
    unittest.main()
