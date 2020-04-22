"""
Yuchen Yao
HW07 Test
this assignment is going to test the 3 tasks in HW06 .
"""

import unittest
from HW07 import anagram_lst, anagram_dd, anagram_cntr, covers_alphabet, web_analyzer
from typing import List, Tuple


class AnagramLstTest(unittest.TestCase):
    def test_anagram_lst(self):
        str1: str = "iceman"
        str2: str = "cinema"
        str3: str = "asasasa"
        str4: str = ""
        self.assertTrue(anagram_lst(str1, str2))
        self.assertFalse(anagram_lst(str1, str3))
        self.assertFalse(anagram_lst(str1, str4))


class AnagramDdTest(unittest.TestCase):
    def test_anagram_dd(self):
        str1: str = "iceman"
        str2: str = "cinema"
        str3: str = "asasasa"
        str4: str = ""
        str5: str = "abc"
        str6: str = "abcd"
        self.assertTrue(anagram_dd(str1, str2))
        self.assertFalse(anagram_dd(str1, str3))
        self.assertFalse(anagram_dd(str1, str4))
        self.assertFalse(anagram_dd(str5, str6))


class AnagramCntrTest(unittest.TestCase):
    def test_anagram_cntr(self):
        str1: str = "iceman"
        str2: str = "cinema"
        str3: str = "asasasa"
        str4: str = ""
        self.assertTrue(anagram_cntr(str1, str2))
        self.assertFalse(anagram_cntr(str1, str3))
        self.assertFalse(anagram_cntr(str1, str4))


class CoversAlphabetTest(unittest.TestCase):
    def test_covers_alphabet(self):
        self.assertTrue(covers_alphabet("AbCdefghiJklomnopqrStuvwxyz"))
        self.assertTrue(covers_alphabet("We promptly judged antique ivory buckles for the next prize"))
        self.assertFalse(covers_alphabet("abc"))


class WebAnalyzerTest(unittest.TestCase):
    def test_web_analyzer(self):
        weblogs: List[Tuple[str, str]] = [
            ('Nanda', 'google.com'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Nanda', 'python.org'),
            ('Fei', 'dzone.com'), ('Nanda', 'google.com'),
            ('Maha', 'google.com'), ]

        summary: List[Tuple[str, List[str]]] = [
            ('dzone.com', ['Fei']),
            ('google.com', ['Maha', 'Nanda']),
            ('python.org', ['Fei', 'Nanda']), ]

        self.assertEqual(web_analyzer(weblogs), summary)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
