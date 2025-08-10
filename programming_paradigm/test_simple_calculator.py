# test_simple_calculator.py
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
