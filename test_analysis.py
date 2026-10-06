import unittest
from analysis import (
    calculate_mean,
    calculate_median,
    calculate_variance,
    calculate_standard_deviation,
    calculate_range,
    detect_outliers
)
class TestAnalysis(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(calculate_mean([10, 20, 30, 40]), 25.0)
    def test_median(self):
        self.assertEqual(calculate_median([10, 20, 30, 40]), 25.0)
    def test_variance(self):
        self.assertEqual(calculate_variance([10, 20, 30, 40]), 125.0)
    def test_range(self):
        self.assertEqual(
            calculate_range([10, 20, 30, 40]),
            (10, 40, 30)
        )
    def test_outliers(self):
        self.assertEqual(
            detect_outliers([10, 11, 12, 13, 14, 100]),
            [100]
        )
    def test_mean_empty_list(self):
      with self.assertRaises(ValueError):
        calculate_mean([])
    def test_empty_data(self):
      with self.assertRaises(ValueError):
        calculate_median([])

      with self.assertRaises(ValueError):
        calculate_range([])

      with self.assertRaises(ValueError):
        detect_outliers([])
if __name__ == "__main__":
    unittest.main()
