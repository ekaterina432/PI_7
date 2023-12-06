import unittest
from main import fibonacci
class TestFibonacci(unittest.TestCase):
    def test_fibonacci_with_positive_number(self):
        self.assertEqual(fibonacci(5), [1, 1, 2, 3, 5])
    def test_fibonacci_with_zero(self):
        self.assertEqual(fibonacci(0), [])
    def test_fibonacci_with_negative_number(self):
        self.assertEqual(fibonacci(-5), [])
    def test_fibonacci_with_large_number(self):
        self.assertEqual(fibonacci(15), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610])

if __name__ == '__main__':
    unittest.main()
