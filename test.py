import unittest
from calcutor import *

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        # Test basic addition
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(100, 200), 300)

    def test_subtract(self):
        # Test basic subtraction
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        # Test basic multiplication
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(100, 0), 0)

    def test_divide(self):
        # Test basic division
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(5, 2), 2.5)
        
        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
