import unittest
from simpleduration import Duration, InvalidDuration

SINGLE_TEST_CASES = [
    ("1 second", 1),
    ("1s", 1),
    ("30 seconds", 30),
    ("30s", 30),
    ("1 minute", 60),
    ("1m", 60),
    ("1.5 minutes", 90),
    ("1.5m", 90),
    ("1 hour", 3600),
    ("1h", 3600),
    ("1.5 hours", 5400),
    ("1.5h", 5400),
    ("1.5H", 5400),
    ("1.5HOURS", 5400),
    ("1.5 HOURS", 5400),
    ("1 day", 3600 * 24),
]

COMBINED_TEST_CASES = [
    ("1m2s", 62),
    ("1h2m", 3720),
    ("1h2s", 3602),
    ("5 minutes 20 seconds", 320),
    ("1.5 hours 30 seconds", 5430),
    ("1 day, 1.5hours, 30 seconds", 91830),
]

INVALID_TEST_CASES = [
    "1foo",
    "bar",
    "13",
    "minute1",
]


class ParseTest(unittest.TestCase):
    def test_single_cases(self):
        for s, expected in SINGLE_TEST_CASES:
            d = Duration(s)
            self.assertEqual(int(d.timedelta().total_seconds()), expected)

    def test_combined_cases(self):
        for s, expected in COMBINED_TEST_CASES:
            d = Duration(s)
            self.assertEqual(int(d.timedelta().total_seconds()), expected)

    def test_invalid_cases(self):
        for s in INVALID_TEST_CASES:
            self.assertRaises(InvalidDuration, Duration, s)
