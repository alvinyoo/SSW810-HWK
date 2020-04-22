"""
Created on Tue Oct 7 2019

@author: Lin Zheng

Test cases for HW05_Lin_Zheng.
"""

import unittest

from HW06_Lin_Zheng import list_copy, list_intersect, list_difference, remove_vowels, check_pwd, insertion_sort

class TestList(unittest.TestCase):
    """ Test of List class

        - Test for the six functions

    """
    def test_list_copy(self):
        """ test_list_copy """
        self.assertEqual(list_copy([1, 3, 5]), [1, 3, 5])
        self.assertEqual(list_copy([]), [])

    def test_list_intersect(self):
        """ test_list_intersect """
        self.assertEqual(list_intersect([1, 3, 5], [1, 2, 3]), [1, 3])
        self.assertEqual(list_intersect([1, 3, 5], [2, 4, 6]), [])
        self.assertEqual(list_intersect([], []), [])

    def test_list_difference(self):
        """ test_list_difference """
        self.assertEqual(list_difference([1, 3, 5], [1, 2, 3]), [5])
        self.assertEqual(list_difference([1, 3, 5], [2, 4, 6]), [1, 3, 5])
        self.assertEqual(list_intersect([], []), [])

    def test_remove_vowels(self):
        """ test_remove_vowels """
        self.assertEqual(remove_vowels('HELLO world!'), 'HLL wrld!')
        self.assertEqual(remove_vowels('hmm shh'), 'hmm shh')
        self.assertEqual(remove_vowels(''), '')

    def test_check_pwd(self):
        """ test_remove_vowels """
        self.assertEqual(check_pwd('Ab'), False)
        self.assertEqual(check_pwd('ab1'), False)
        self.assertEqual(check_pwd('AB1'), False)
        self.assertEqual(check_pwd('Ab1'), True)
        self.assertEqual(check_pwd(''), False)

    def test_insertion_sort(self):
        """ test_insertion_sort """
        self.assertEqual(insertion_sort([1, 5, 3, 3]), [1, 3, 3, 5])
        self.assertEqual(insertion_sort([]), [])

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)