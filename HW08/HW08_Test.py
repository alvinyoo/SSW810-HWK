"""
Yuchen Yao
HW08 Test
this assignment is going to test the 3 tasks in HW08 .
"""


import unittest
from HW08 import date_arithmetic, file_reader, FileAnalyzer
from datetime import datetime
import os


class DateArithmeticTest(unittest.TestCase):
    def test_date_arithmetic(self):
        dat1: datetime = datetime.strptime("Mar 1, 2020", "%b %d, %Y")
        dat2: datetime = datetime.strptime("Mar 2, 2019", "%b %d, %Y")
        self.assertEqual(date_arithmetic(), (dat1, dat2, 241))


class FieldReaderTest(unittest.TestCase):
    def test_field_reader(self):
        path = 'text1.txt'
        expect = (('123', 'Jin He', 'Computer Science'), ('234', 'Nanda Koka', 'Software Engineering'),
                  ('345', 'Benji Cai', 'Software Engineering'))
        result = tuple(file_reader(path, 3, sep='|', header=True))

        self.assertEqual(result, expect)


class FileAnalyzerTest(unittest.TestCase):
    path = '/Users/yaoyuchen/Documents/SSW810/HWK&ASMT/test'
    fa = FileAnalyzer(path)
    print(fa.files_summary)
    fa.pretty_print()


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
