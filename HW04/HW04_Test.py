"""
Yuchen Yao
HW04
this assignment is going to test the 4 tasks in HW04 .
"""


import unittest
from typing import Optional
from HW04 import count_vowels, find_last, my_enumerate


# PART 1 TEST
class CountVowelsTest(unittest.TestCase):
    def test_count_vowels(self) -> None:
        """ testing count vowels """
        cv1: int = count_vowels('hello')
        cv2: int = count_vowels('WORLD')
        cv3: int = count_vowels('hello WORLD')
        cv4: int = count_vowels('hll WRLD')
        self.assertEqual(cv1, 2)
        self.assertEqual(cv2, 1)
        self.assertEqual(cv3, 3)
        self.assertEqual(cv4, 0)


# PART 2 TEST
class FindLastTest(unittest.TestCase):
    def test_find_last(self) -> None:
        """ testing find_last """
        fl1: Optional[int] = find_last('h', 'hello')
        fl2: Optional[int] = find_last('l', 'hello')
        fl3: Optional[int] = find_last('a', 'hello')
        test_list: list = [42, 33, 21, 33]
        fl4: Optional[int] = find_last(33, test_list)
        self.assertEqual(fl1, 0)
        self.assertEqual(fl2, 3)
        self.assertEqual(fl3, None)
        self.assertEqual(fl4, 3)


# PART 4 TEST
class EnumerateTest(unittest.TestCase):
    def test_enumerate_list(self) -> None:
        """ test my_enumerate by storing the results in a list """
        seq1 = "hello world"
        seq2 = [1, 2, 3, 4]
        self.assertEqual(list(enumerate(seq1)), list(my_enumerate(seq1)))
        self.assertEqual(list(enumerate(seq2)), list(my_enumerate(seq2)))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
