import unittest
from main import func

class TestFunc(unittest.TestCase):

    def test_pos(self):
        self.assertEqual(func(5), 25)

    def test_neg(self):
        self.assertEqual(func(-4), 16)

    def test_zero(self):
        self.assertEqual(func(0), 0)

if __name__ == '__main__':
    unittest.main()