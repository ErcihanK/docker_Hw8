import unittest
from app import Calculator

class TestArithmeticOperations(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(1, 1), 2)
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(10, -5), 15)

if __name__ == '__main__':
    unittest.main()
