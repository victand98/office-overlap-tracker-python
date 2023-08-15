import unittest
from src.scheduler import calculate_overlap


class TestCalculateOverlap(unittest.TestCase):
    def test_no_overlap(self):
        schedule1 = [['MO', '10:00', '12:00']]
        schedule2 = [['TU', '13:00', '14:00']]
        overlap_count = calculate_overlap(schedule1, schedule2)
        self.assertEqual(overlap_count, 0)

    def test_overlap(self):
        schedule1 = [['MO', '10:00', '12:00']]
        schedule2 = [['MO', '11:00', '13:00']]
        overlap_count = calculate_overlap(schedule1, schedule2)
        self.assertEqual(overlap_count, 1)


if __name__ == '__main__':
    unittest.main()
