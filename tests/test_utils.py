import unittest
from src.utils import parse_time, calculate_time_overlap


class TestUtils(unittest.TestCase):
    def test_parse_time(self):
        time_range = 'MO10:00-12:00'
        parsed_time = parse_time(time_range)
        self.assertEqual(parsed_time, ['MO', '10:00', '12:00'])

    def test_calculate_time_overlap(self):
        self.assertTrue(calculate_time_overlap(
            '10:00', '12:00', '11:00', '13:00'))
        self.assertFalse(calculate_time_overlap(
            '10:00', '12:00', '13:00', '14:00'))


if __name__ == '__main__':
    unittest.main()
