"""
Yuchen Yao
HW10
test data in University
"""

import unittest
from .HW11 import University, PrettyTable


path: str = '/Users/yaoyuchen/Documents/SSW810/HWK&ASMT/HW11'


class TestUniversity(unittest.TestCase):
    """ test class University from HW09 """
    def test_student(self) -> None:
        calculated: dict = {}
        for cwid, student in University(path).students.items():
            calculated[cwid] = [student.CWID, student.name,
                                sorted(student.completed_courses), sorted(student.remain_req),
                                sorted(student.remain_ele), student.gpa]

        exp: dict = {'10103': ['10103', 'Jobs, S', ['CS 501', 'SSW 810'], ['SSW 540', 'SSW 555'], [], 3.38],
                     '10115': ['10115', 'Bezos, J', ['SSW 810'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 546'], 2.0],
                     '10183': ['10183', 'Musk, E', ['SSW 555', 'SSW 810'], ['SSW 540'], ['CS 501', 'CS 546'], 4.0],
                     '11714': ['11714', 'Gates, B', ['CS 546', 'CS 570', 'SSW 810'], [], [], 3.5]}
        self.assertEqual(calculated, exp)

    def test_instructor(self) -> None:
        exp: dict = {'98764': ('98764', 'Cohen, R', 'SFEN', {'CS 546': 1}),
                     '98763': ('98763', 'Rowland, J', 'SFEN', {'SSW 810': 4, 'SSW 555': 1}),
                     '98762': ('98762', 'Hawking, S', 'CS', {'CS 501': 1, 'CS 546': 1, 'CS 570': 1})}
        calculated: dict = {}
        for cwid, instructor in University(path).instructors.items():
            calculated[cwid] = (cwid, instructor.name, instructor.dept, dict(instructor.courses))
        self.assertEqual(calculated, exp)

    def test_major(self) -> None:
        majors: dict = University(path).majors

        self.assertEqual(majors['SFEN'].req, ['SSW 540', 'SSW 810', 'SSW 555'])
        self.assertEqual(majors['SFEN'].ele, ['CS 501', 'CS 546'])
        self.assertEqual(majors['CS'].req, ['CS 570', 'CS 546'])
        self.assertEqual(majors['CS'].ele, ['SSW 810', 'SSW 565'])

    def test_student_grades_table_db(self):
        university: University = University(path)
        table: PrettyTable = university.student_grades_table_db(path + '/HW11.db')
        print(table.get_string())
        string = "+----------+-------+---------+-------+------------+\n" \
                 "|   Name   |  CWID |  Course | Grade | Instructor |\n" \
                 "+----------+-------+---------+-------+------------+\n" \
                 "| Bezos, J | 10115 | SSW 810 |   A   | Rowland, J |\n" \
                 "| Bezos, J | 10115 |  CS 546 |   F   | Hawking, S |\n" \
                 "| Gates, B | 11714 | SSW 810 |   B-  | Rowland, J |\n" \
                 "| Gates, B | 11714 |  CS 546 |   A   |  Cohen, R  |\n" \
                 "| Gates, B | 11714 |  CS 570 |   A-  | Hawking, S |\n" \
                 "| Jobs, S  | 10103 | SSW 810 |   A-  | Rowland, J |\n" \
                 "| Jobs, S  | 10103 |  CS 501 |   B   | Hawking, S |\n" \
                 "| Musk, E  | 10183 | SSW 555 |   A   | Rowland, J |\n" \
                 "| Musk, E  | 10183 | SSW 810 |   A   | Rowland, J |\n" \
                 "+----------+-------+---------+-------+------------+"

        self.assertEqual(table.get_string(), string)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
