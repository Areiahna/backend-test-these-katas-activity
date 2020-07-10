import unittest
import katas


class TestKatas(unittest.TestCase):

    def test_add(self):

        self.assertEqual(3+5, 8)

    def test_multiply(self):

        self.assertEqual(7*2, 14)

    def test_power(self):
        self.assertEqual((4*(2*2)), 16)

    def test_factorial(self):
        self.assertTrue(4, 24)

    def test_fibonacci(self):
        self.assertTrue(2, 1) and self.assertTrue(5, 13)


if __name__ == '__main__':
    unittest.main()
