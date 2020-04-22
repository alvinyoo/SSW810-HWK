"""
Created on Tue Oct 25 2019

@author: Lin Zheng

Test cases for HW08_Lin_Zheng.
"""

import unittest

from HW08_Lin_Zheng import date_arithmetic, file_reading_gen, FileAnalyzer

class TestModuleGeneratorFile(unittest.TestCase):
    """ Test of ModuleGeneratorFile

        - Test for the functions

    """
    def test_date_arithmetic(self):
        """ test_date_arithmetic """
        self.assertEqual(date_arithmetic(), ('03/01/2000', '03/02/2017', 303))

    def test_file_reading_gen(self):
        """ test_file_reading_gen """
        path = '/Users/LSM/Desktop/test2.txt'
        expect = (('123', 'Jin He', 'Computer Science'), ('234', 'Nanda Koka', 'Software Engineering'), \
                 ('345', 'Benji Cai', 'Software Engineering'))
        result = tuple(file_reading_gen(path, 3, sep='|', header=True))
        self.assertEqual(result, expect)

    def test_FileAnalyzer(self):
        """ test_FileAnalyzer """
        result = FileAnalyzer('C:\\Users\\LSM\\Desktop\\Test files').files_summary
        expect = {'C:\\Users\\LSM\\Desktop\\Test files\\0_defs_in_this_file.py': \
                 {'class': 0, 'function': 0, 'line': 3, 'char': 57}, \
                 'C:\\Users\\LSM\\Desktop\\Test files\\file1.py': \
                 {'class': 2, 'function': 4, 'line': 25, 'char': 270}}
        self.assertEqual(result, expect)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    print(FileAnalyzer('C:\\Users\\LSM\\Desktop\\Test files').pretty_print())