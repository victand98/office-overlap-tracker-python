import unittest
from src.reader import read_input


class TestReadInput(unittest.TestCase):
    def test_read_input(self):
        data = read_input('test_input.txt')
        expected_data = {
            'RENE': [['MO', '10:00', '12:00'], ['TU', '10:00', '12:00']],
            'ASTRID': [['MO', '10:00', '12:00'], ['TH', '12:00', '14:00']],
            'ANDRES': [['MO', '10:00', '12:00'], ['TH', '12:00', '14:00']]
        }
        self.assertEqual(data, expected_data)


if __name__ == '__main__':
    unittest.main()
