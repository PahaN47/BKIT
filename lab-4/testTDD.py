from prog import biquad_roots
from prog import is_real
import unittest

class biquad_test(unittest.TestCase):
    def test1(self):
        self.assertEqual(biquad_roots(1), [0])
    def test2(self):
        self.assertEqual(biquad_roots(1, -1, 0), [-1, 0, 1])
    def test3(self):
        self.assertEqual(biquad_roots(1, 1, -6), [-2**0.5, 2**0.5])
    def test4(self):
        self.assertEqual(biquad_roots(-1, 4, -3), [-3**0.5, -1, 1, 3**0.5])
    def test5(self):
        self.assertEqual(biquad_roots(2, 0, 1), [])
    def test6(self):
        self.assertEqual(biquad_roots(0, 1, 1), [])

    def test7(self):
        self.assertFalse(is_real('5'))
    def test8(self):
        self.assertFalse(is_real('-4.5'))
    def test9(self):
        self.assertFalse(is_real('route'))
    def test10(self):
        self.assertTrue(is_real(33))
    def test11(self):
        self.assertTrue(is_real(-6.3))

if __name__ == '__main__':
    unittest.main()
    