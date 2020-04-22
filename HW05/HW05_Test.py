"""
Yuchen Yao
HW04
this assignment is going to test the 4 tasks in HW05 .
"""


import unittest
from typing import List
from HW05 import reverse, substring, find_second, get_lines


# PART 1 TEST
class ReverseTest(unittest.TestCase):
    def test_reverse(self) -> None:
        """ testing reverse argument """
        s: str = "abc"
        self.assertTrue(reverse(s) == "cba")


# PART 2 TEST
class SubstringTest(unittest.TestCase):
    def test_substring(self) -> None:
        """ testing find target from a string """
        i1: int = substring("he", "hello")
        i2: int = substring("ell", "hello")
        i3: int = substring("xxx", "hello")
        self.assertEqual(i1, 0)
        self.assertEqual(i2, 1)
        self.assertEqual(i3, -1)


# PART 3 TEST
class FindSecondTest(unittest.TestCase):
    def test_find_second(self) -> None:
        """ testing find second target from a string """
        i1: int = find_second('iss', 'Mississippi')
        i2: int = find_second('abba', 'abbabba')
        i3: int = find_second('xxx', 'abbabba')
        i4: int = find_second('XX', 'aXXbcd')
        i5: int = find_second('ab', 'abababab')
        self.assertEqual(i1, 4)
        self.assertEqual(i2, 3)
        self.assertEqual(i3, -1)
        self.assertEqual(i4, -1)
        self.assertEqual(i5, 2)


# PART 4 TEST
class GetLinesTest(unittest.TestCase):
    def test_get_lines(self) -> None:
        """ testing get_lines function """
        file_name: str = 'text1.txt'
        expect: List[str] = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>', '<line4.1 line4.2>',
                             '<line5>', '<line6>']
        result: List[str] = list(get_lines(file_name))
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
