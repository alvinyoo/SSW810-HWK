"""
Created on Tue Oct 16 2019

@author: Lin Zheng

Test cases for HW07_Lin_Zheng.
"""

import unittest

from HW07_Lin_Zheng import anagram_lst, anagrams_dd, anagrams_cntr, covers_alphabet, book_index

class TestContainer(unittest.TestCase):
    """ Test of List class

        - Test for the functions

    """
    def test_anagram_lst(self):
        """ test_anagram_lst """
        self.assertEqual(anagram_lst('cinema', 'iceman'), True)
        self.assertEqual(anagram_lst('dormitory', 'dirtyroom'), True)
        self.assertEqual(anagram_lst('Dormitory', 'dirtyroom'), True)
        self.assertEqual(anagram_lst('abc', 'def'), False)
        self.assertEqual(anagram_lst('aaa', 'abc'), False)
        self.assertEqual(anagram_lst('', ''), True)

    def test_anagrams_dd(self):
        """ test_anagram_dd """
        self.assertEqual(anagrams_dd('cinema', 'iceman'), True)
        self.assertEqual(anagrams_dd('dormitory', 'dirtyroom'), True)
        self.assertEqual(anagrams_dd('abc', 'def'), False)
        self.assertEqual(anagrams_dd('', ''), True)

    def test_anagrams_cntr(self):
        """ test_anagram_cntr """
        self.assertEqual(anagrams_cntr('cinema', 'iceman'), True)
        self.assertEqual(anagrams_cntr('dormitory', 'dirtyroom'), True)
        self.assertEqual(anagram_lst('Dormitory', 'dirtyroom'), True)
        self.assertEqual(anagrams_cntr('abc', 'def'), False)
        self.assertEqual(anagrams_cntr('', ''), True)

    def test_covers_alphabet(self):
        """ test_covers_alphabet """
        self.assertEqual(covers_alphabet('abcdefghijklmnopqrstuvwxyz'), True)
        self.assertEqual(covers_alphabet('aabbcdefghijklmnopqrstuvwxyzzabc'), True)
        self.assertEqual(covers_alphabet('The quick brown fox jumps over the lazy dog'), True)
        self.assertEqual(covers_alphabet('We promptly judged antique ivory buckles for the next prize'), True)
        self.assertEqual(covers_alphabet('xyz'), False)
        self.assertEqual(covers_alphabet(''), False)

    def test_book_index(self):
        """ test_book_index """
        woodchucks = [('how', 3), ('much', 3), ('wood', 3), ('would', 2), \
        ('a', 1), ('woodchuck', 1), ('chuck', 3), ('if', 1), ('a', 1), \
        ('woodchuck', 2), ('could', 2), ('chuck', 1), ('wood', 1)]
        result = [['a', [1]], ['chuck', [1, 3]], ['could', [2]], ['how', [3]], \
        ['if', [1]], ['much', [3]], ['wood', [1, 3]], ['woodchuck', [1, 2]], ['would', [2]]]
        self.assertEqual(book_index(woodchucks), result)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)