"""
Yuchen Yao
HW03
this assignment is going to test the fraction calculator .
"""


import unittest
from HW03 import Fraction


class TestFraction(unittest.TestCase):
    """ test class Fraction """
    def test_init(self) -> None:
        """ verify that the numerator and denominator are set properly """
        f: Fraction = Fraction(3, 4)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)

    def test_init_exception(self) -> None:
        """ verify that ZeroDivisionError is raised when appropriate """
        self.assertRaises(ZeroDivisionError, Fraction, 1, 0)

    def test_str(self) -> None:
        """ verify that the __str__() is set properly """
        f1: Fraction = Fraction(1, 2)
        f2: Fraction = Fraction(-1, 2)
        f3: Fraction = Fraction(1, -2)
        f4: Fraction = Fraction(-1, -2)
        self.assertEqual(str(f1), '1/2')
        self.assertEqual(str(f2), '-1/2')
        self.assertEqual(str(f3), '-1/2')
        self.assertEqual(str(f4), '1/2')

    def test_add(self) -> None:
        """ verify Fraction addition """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 + f34, Fraction(10, 8))
        self.assertEqual(f12, Fraction(1, 2))  # f12 should not have changed

    def test_sub(self) -> None:
        """ verify Fraction subtraction """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 - f34, Fraction(-2, 8))
        self.assertEqual(f34 - f12, Fraction(2, 8))
        self.assertEqual(f12, Fraction(1, 2))  # f12 should not have changed

    def test_mul(self) -> None:
        """ verify Fraction multiplication """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 * f34, Fraction(3, 8))
        self.assertEqual(f12, Fraction(1, 2))  # f12 should not have changed

    def test_truediv(self) -> None:
        """ verify Fraction division """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 / f34, Fraction(4, 6))
        self.assertEqual(f12, Fraction(1, 2))  # f12 should not have changed

    def test_eq(self) -> None:
        """ verify that the __eq__() is work properly """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f24: Fraction = Fraction(2, 4)
        self.assertTrue(f12 == f24)
        self.assertFalse(f12 == f34)

    def test_ne(self) -> None:
        """ verify that the __ne__() is work properly """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f24: Fraction = Fraction(2, 4)
        self.assertTrue(f12 == f24)
        self.assertFalse(f12 == f34)

    def test_lt(self) -> None:
        """ verify that the __lt__() is work properly """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertTrue(f12 < f34)
        self.assertFalse(f12 > f34)

    def test_le(self) -> None:
        """ verify that the __le__() is work properly """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f24: Fraction = Fraction(2, 4)
        self.assertTrue(f12 <= f34)
        self.assertTrue(f12 <= f24)
        self.assertFalse(f34 <= f12)

    def test_gt(self) -> None:
        """ verify that the __ge__() is work properly """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertTrue(f34 > f12)
        self.assertFalse(f12 > f34)

    def test_ge(self) -> None:
        """ verify that the __ge__() is work properly """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f68: Fraction = Fraction(6, 8)
        self.assertTrue(f34 >= f12)
        self.assertTrue(f34 >= f68)
        self.assertFalse(f12 >= f34)

    def test_3_operands(self) -> None:
        """ verify expressions with more than two operands """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f44: Fraction = Fraction(4, 4)
        self.assertTrue(f12 + f34 + f44 == Fraction(72, 32))
        self.assertTrue(f12 - f34 - f44 == Fraction(-5, 4))
        self.assertTrue(f12 * f34 * f44 == Fraction(3, 8))
        self.assertTrue(f12 / f34 / f44 == Fraction(2, 3))

    def test_simplify(self) -> None:
        """ testing the simplify() """
        f1: Fraction = Fraction(9, 27)
        f2: Fraction = Fraction(-9, 27)
        f3: Fraction = Fraction(9, -27)
        f4: Fraction = Fraction(-9, -27)
        self.assertEqual(str(f1.simplify()), '1.0/3.0')
        self.assertEqual(str(f2.simplify()), '-1.0/3.0')
        self.assertEqual(str(f3.simplify()), '-1.0/3.0')
        self.assertEqual(str(f4.simplify()), '1.0/3.0')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
