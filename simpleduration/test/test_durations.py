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


class ComposeTest(unittest.TestCase):
    def test_eq(self):
        d1 = Duration("10 minutes")
        d2 = Duration("10 m")
        d3 = Duration("600 seconds")
        d4 = Duration("601 seconds")
        self.assertTrue(d1 == d2)
        self.assertTrue(d1 == d3)
        self.assertTrue(d3 == d1)
        self.assertTrue(d1 != d4)

    def test_cmp(self):
        d1 = Duration("10 minutes")
        d2 = Duration("601 seconds")
        self.assertTrue(d1 < d2)
        self.assertTrue(d1 <= d2)
        self.assertFalse(d1 > d2)
        self.assertFalse(d1 >= d2)

    def test_arithmetic(self):
        d1 = Duration("10 seconds")
        d2 = Duration("20 seconds")
        self.assertEqual(d1 + d1, d2)
        self.assertEqual(d2 - d1, d1)
        self.assertEqual(d1 * 2, d2)
        self.assertEqual(2 * d1, d2)

        d1 += d1
        self.assertEqual(d1, d2)

        d2 -= d1
        self.assertEqual(d2, 0.0)
