import unittest
import os
import pandas as pd
from data_loader import load_data
class TestDataLoader(unittest.TestCase):
    def test_valid_csv(self):
        filename = "test_valid.csv"
        with open(filename, "w") as file:
            file.write("value\n10\n20\n30\n")
        result = load_data(filename)
        self.assertEqual(result, [10, 20, 30])
        os.remove(filename)
    def test_missing_value_column(self):
       filename = "test_wrong.csv"
       with open(filename, "w") as file:
          file.write("price\n10\n20\n30\n")
       with self.assertRaises(ValueError):
           load_data(filename)
       os.remove(filename)
    def test_non_numeric_data(self):
       filename = "test_invalid.csv"
       with open(filename, "w") as file:
          file.write("value\n10\nhello\n30\n")
       with self.assertRaises(ValueError):
         load_data(filename)
       os.remove(filename)
if __name__ == "__main__":
    unittest.main()