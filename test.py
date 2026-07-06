import main
import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = main.add(10, 5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = main.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_multiply(self):
        result = main.multiply(10, 5)
        self.assertEqual(result, 50)

    def test_divide(self):
        result = main.divide(10, 5)
        self.assertEqual(result, 2)

    def test_divide_by_zero(self):
        result = main.divide(10, 0)
        self.assertEqual(result, "Cannot divide by zero")

if __name__ == "__main__":
    unittest.main()