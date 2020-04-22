"""
Yuchen Yao
HW10
test data in University
"""

import unittest
from HW10 import Student, Instructor, University


path: str = '/Users/yaoyuchen/Documents/SSW810/HWK&ASMT'


class TestUniversity(unittest.TestCase):
    """ test class University from HW09 """
    def test_student(self) -> None:
        calculated: dict = {}
        for cwid, student in University(path).students.items():
            calculated[cwid] = [student.CWID, student.name,
                                sorted(student.completed_courses), sorted(student.remain_req),
                                sorted(student.remain_ele), student.gpa]

        exp: dict = {'10103': ['10103', 'Baldwin, C', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [], 3.44],
                     '10115': ['10115', 'Wyatt, X', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [], 3.81],
                     '10172': ['10172', 'Forbes, I', ['SSW 555', 'SSW 567'], ['SSW 540', 'SSW 564'], ['CS 501', 'CS 513', 'CS 545'], 3.88],
                     '10175': ['10175', 'Erickson, D', ['SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 513', 'CS 545'], 3.58],
                     '10183': ['10183', 'Chapman, O', ['SSW 689'], ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545'], 4.0],
                     '11399': ['11399', 'Cordova, I', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [], 3.0],
                     '11461': ['11461', 'Wright, U', ['SYS 611', 'SYS 750', 'SYS 800'], ['SYS 612', 'SYS 671'], ['SSW 540', 'SSW 565', 'SSW 810'], 3.92],
                     '11658': ['11658', 'Kelly, P', [], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'], 0.0],
                     '11714': ['11714', 'Morton, A', ['SYS 611', 'SYS 645'], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'], 3.0],
                     '11788': ['11788', 'Fuller, E', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [], 4.0]
                     }

        self.assertEqual(calculated, exp)

    def test_instructor(self) -> None:
        exp: dict = {
            '98765': ('98765', 'Einstein, A', 'SFEN', {'SSW 567': 4, 'SSW 540': 3}),
            '98764': ('98764', 'Feynman, R', 'SFEN', {'SSW 564': 3, 'SSW 687': 3, 'CS 501': 1, 'CS 545': 1}),
            '98763': ('98763', 'Newton, I', 'SFEN', {'SSW 555': 1, 'SSW 689': 1}),
            '98762': ('98762', 'Hawking, S', 'SYEN', {}),
            '98761': ('98761', 'Edison, A', 'SYEN', {}),
            '98760': ('98760', 'Darwin, C', 'SYEN', {'SYS 800': 1, 'SYS 750': 1, 'SYS 611': 2, 'SYS 645': 1})
        }
        calculated: dict = {}
        for cwid, instructor in University(path).instructors.items():
            calculated[cwid] = (cwid, instructor.name, instructor.dept, dict(instructor.courses))

        self.assertEqual(calculated, exp)

    def test_major(self) -> None:
        majors: dict = University(path).majors

        self.assertEqual(majors['SFEN'].req, ['SSW 540', 'SSW 564', 'SSW 555', 'SSW 567'])
        self.assertEqual(majors['SFEN'].ele, ['CS 501', 'CS 513', 'CS 545'])
        self.assertEqual(majors['SYEN'].req, ['SYS 671', 'SYS 612', 'SYS 800'])
        self.assertEqual(majors['SYEN'].ele, ['SSW 810', 'SSW 565', 'SSW 540'])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
