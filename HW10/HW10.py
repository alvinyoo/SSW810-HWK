"""
Yuchen Yao
HW10
"""


from HW08_Yuchen_Yao import file_reader
from prettytable import PrettyTable
from typing import DefaultDict, Tuple, Iterator, List, Any
from collections import defaultdict


class Major:
    """
    define the required and elective courses for a major
    """
    def __init__(self, dept: str) -> None:
        self.dept: str = dept
        self.req: list = []
        self.ele: list = []

    def add_course(self, flag: str, course: str) -> None:
        if flag.lower() == 'r':
            self.req.append(course)
        elif flag.lower() == 'e':
            self.ele.append(course)
        else:
            raise ValueError(f"Unexpected flag '{flag}' ")

    def remain_required(self, courses: set) -> list:
        remain_r: list = []
        for c in self.req:
            if c not in courses:
                remain_r.append(c)
        return remain_r

    def remain_elective(self, courses: set) -> Any:
        if courses.intersection(self.ele):
            return []
        else:
            return self.ele

    def passed_courses(self, courses: dict) -> list:
        grades: List[str] = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']
        course: str
        grade: str
        p_courses: list = []

        for course, grade in courses.items():
            if grade in grades:
                p_courses.append(course)

        return p_courses


class Student:
    """
    class Student holds all of the details of a student,
    including cwid, name, major and their courses with grades.
    """

    student_fields: List[str] = ['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required',
                                 'Remaining Electives', 'GPA']

    def __init__(self, CWID: int, name: str, major: Major, courses: dict, gpa: float) -> None:
        self.CWID: int = CWID
        self.name: str = name
        self.major: Major = major
        self.courses: dict = courses
        self.completed_courses: list = []
        self.remain_req: list = []
        self.remain_ele: list = []
        self.gpa: float = gpa

    def __str__(self) -> str:
        return str((self.CWID, self.name, self.major, self.courses))

    def add_courses(self, course: str, grade: str) -> None:
        self.courses[course]: str = grade

    def update_gpa(self) -> None:
        t_value: float = 0
        gpa_map: dict = {'A': 4, 'A-': 3.75, 'B+': 3.25, 'B': 3, 'B-': 2.75, 'C+': 2.25, 'C': 2.00}
        for course in self.completed_courses:
            t_value += gpa_map.get(self.courses[course], 0)
        self.gpa = round(t_value / len(self.courses), 2)


class Instructor:
    """
    class Instructor holds all of the details of an instructor,
    including cwid, name, dept and courses along with the number of students who have taken the course.
    """

    instructor_fields: List[str] = ['CWID', 'Name', 'Department', 'Course', 'Students']

    def __init__(self, CWID: int, name: str, dept: str) -> None:
        self.CWID: int = CWID
        self.name: str = name
        self.dept: str = dept
        self.courses: DefaultDict = defaultdict(int)

    def __str__(self):
        return str((self.CWID, self.name, self.dept, self.courses))

    def add_student(self, course) -> None:
        self.courses[course] += 1


class University:
    """
    class University holds all of the students, instructors and grades for a single University
    """
    def __init__(self, path: str) -> None:
        self.path: str = path
        self.students: dict = {}
        self.instructors: dict = {}
        self.majors: dict = {}

        self.load_majors(path + '/majors.txt')
        self.load_student(path + '/students.txt')
        self.load_instructor(path + '/instructors.txt')
        self.load_grade(path + '/grades.txt')
        self.update_course()

        self.major_pretty_table()
        self.student_pretty_table()
        self.instructor_pretty_table()

    def load_majors(self, path) -> None:
        fp_m: Iterator[Tuple[str]] = file_reader(path, 3, sep='\t', header=True)
        dept: str
        flag: str
        course: str

        try:
            for dept, flag, course in fp_m:
                if dept not in self.majors.keys():
                    self.majors[dept] = Major(dept)
                self.majors[dept].add_course(flag, course)
        except ValueError as err:
            print(err)
        except FileNotFoundError as err:
            print(err)

    def load_student(self, path: str) -> None:
        fp_s: Iterator[Tuple[str]] = file_reader(path, 3, sep=';', header=True)
        CWID: int
        name: str
        major_name: str

        try:
            for CWID, name, major_name in fp_s:
                if CWID in self.students:
                    print('Duplicated student.')
                elif major_name not in self.majors:
                    print(f"{CWID}: {name} has a unknown major {major_name}")
                else:
                    major: Major = self.majors[major_name]
                    self.students[CWID] = Student(CWID, name, major, {}, 0)
        except FileNotFoundError as err:
            print(err)
            # sys.exit(1)
        except ValueError as err:
            print(err)
            # sys.exit(1)

    def load_instructor(self, path: str) -> None:
        fp_i: Iterator[Tuple[str]] = file_reader(path, 3, sep='|', header=True)
        CWID: int
        name: str
        dpt: str

        try:
            for CWID, name, dpt in fp_i:
                if CWID in self.instructors:
                    print('Duplicated instructor.')
                else:
                    self.instructors[CWID] = Instructor(CWID, name, dpt)
        except FileNotFoundError as err:
            print(err)
        except ValueError as err:
            print(err)

    def load_grade(self, path: str) -> None:
        fp_g: Iterator[Tuple[str]] = file_reader(path, 4, sep='|', header=True)
        student_cwid: int
        course: str
        letter_grade: str
        instructor_cwid: int

        try:
            for student_cwid, course, letter_grade, instructor_cwid in fp_g:
                if student_cwid not in self.students:
                    raise ValueError(f"There's a unknown student with CWID: {student_cwid}")
                if instructor_cwid not in self.instructors:
                    raise ValueError(f"There's a grade from unknown instructor: {instructor_cwid}")

                self.students[student_cwid].add_courses(course, letter_grade)
                self.instructors[instructor_cwid].add_student(course)
        except FileNotFoundError as err:
            print(err)
        except ValueError as err:
            print(err)

    def update_course(self):
        for student in self.students.values():
            student.completed_courses = sorted([course for course, grade in student.courses.items() if grade in
                                         ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']])
            student.remain_req = sorted(student.major.remain_required(set(student.completed_courses)))
            student.remain_ele = sorted(student.major.remain_elective(set(student.completed_courses)))
            student.update_gpa()


    def major_pretty_table(self) -> None:
        major_table: PrettyTable = PrettyTable(field_names=['Major', 'Required', 'Electives'])

        for major in self.majors.values():
            arr: List[Any] = [major.dept,
                              sorted([course for course in major.req]),
                              sorted([course for course in major.ele])]
            major_table.add_row(arr)

        print(major_table)

    def student_pretty_table(self) -> None:
        student_table: PrettyTable = PrettyTable(field_names=['CWID', 'Name', 'Major', 'Completed Courses',
                                                              'Remaining Required', 'Remaining Elective', 'GPA'])
        student: Any

        for student in self.students.values():
            arr: List[Any] = [student.CWID, student.name, student.major.dept, student.completed_courses,
                              student.remain_req, student.remain_ele, student.gpa]
            student_table.add_row(arr)

        print(student_table)

    def instructor_pretty_table(self) -> None:
        instructor_table: PrettyTable = PrettyTable(field_names=['CWID', 'Name', 'Dept', 'Course', 'Students'])
        instructor: Any
        for instructor in self.instructors.values():
            for course in instructor.courses:
                arr: List[Any] = [instructor.CWID, instructor.name, instructor.dept, course, instructor.courses[course]]
                instructor_table.add_row(arr)

        print(instructor_table)


def main() -> None:
    path: str = '/Users/yaoyuchen/Documents/SSW810/HWK&ASMT'
    University(path)


if __name__ == '__main__':
    main()
