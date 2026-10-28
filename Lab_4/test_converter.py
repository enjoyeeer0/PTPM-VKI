import unittest
import sys
import os

# Добавляем родительскую папку в путь для импорта
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Lab_4.converter import Converter


class TestConverter(unittest.TestCase):

    # === Диапазон [100.7; +inf) ===
    def test_x_equals_100_7(self):
        self.assertEqual(Converter.do(100.7), 1000)

    def test_x_greater_than_100_7(self):
        self.assertEqual(Converter.do(500.3), 1000)

    # === Диапазон (0; 100.7) ===
    def test_x_positive_small(self):
        self.assertEqual(Converter.do(0.1), 0)

    def test_x_positive_middle(self):
        self.assertEqual(Converter.do(65.7), 65)

    def test_x_boundary_100_6(self):
        self.assertEqual(Converter.do(100.6), 100)

    # === x == 0.0 ===
    def test_x_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            Converter.do(0.0)

    # === Диапазон [-30.4; 0) ===
    def test_x_negative_small(self):
        self.assertEqual(Converter.do(-0.1), -5)

    def test_x_boundary_minus_30_4(self):
        self.assertEqual(Converter.do(-30.4), -35)

    def test_x_negative_middle(self):
        self.assertEqual(Converter.do(-15.2), -20)

    # === Диапазон (-inf; -30.5] ===
    def test_x_boundary_minus_30_5(self):
        self.assertEqual(Converter.do(-30.5), -2000)

    def test_x_very_negative(self):
        self.assertEqual(Converter.do(-94.5), -2000)


if __name__ == '__main__':
    unittest.main()