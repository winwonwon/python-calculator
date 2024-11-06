import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(5, 4), 9)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)
        self.assertEqual(self.calc.subtract(9, 4), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(1, 2), 2)
        self.assertEqual(self.calc.multiply(5, 4), 20)

    def test_divide(self):
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(15, 3), 5)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(19, 6), 1)
        self.assertEqual(self.calc.modulo(14, 6), 2)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()