"""
HW08
this homework contained 3 tasks
"""


from typing import Tuple, Iterator, IO, Any
from datetime import datetime, timedelta
import os
from prettytable import PrettyTable



# PART 1
def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """ Code segment demonstrating expected return values """
    three_days_after_02272020: datetime = datetime.strptime("Feb 27, 2020", "%b %d, %Y") + timedelta(days=3)
    three_days_after_02272019: datetime = datetime.strptime("Feb 27, 2019", "%b %d, %Y") + timedelta(days=3)
    days_passed_01022019_09302019: int = (datetime.strptime("Sep 30, 2019", "%b %d, %Y") -
                                          datetime.strptime("Feb 1, 2019", "%b %d, %Y")).days

    return three_days_after_02272020, three_days_after_02272019, days_passed_01022019_09302019


# PART 2
def file_reader(path: str, fields: int, sep: str = ',', header: bool = False) -> Iterator[Tuple[str]]:
    """ Reading text files with a fixed number of fields, separated by a specific character """
    try:
        fp: IO = open(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: file not found '{path}'")

    with fp:
        index: int

        if header:
            fp.readline()

        for index, ln in enumerate(fp):
            line: tuple = tuple(ln.rstrip('\n').split(sep))

            if len(line) != fields:
                raise ValueError(f'Error: {path} has {len(line)} fields on line {index + 1} but expected {fields}')

            else:
                yield line
                index += 1


# PART 3
class FileAnalyzer:
    def __init__(self, directory):
        self.directory = directory # NOT mandatory!
        self.files_summary = dict()
        self.table = PrettyTable()
        self.table.field_names = ['File Name', 'Classes', 'Functions', 'Lines', 'Characters']
        self.analyze_files() # summerize the python files data


    def analyze_files(self):
        for file in os.listdir(self.directory):
            try:
                fp: IO = open(self.directory + '/' + file)
            except FileNotFoundError:
                raise FileNotFoundError(f"file not found '{file}'")

            with fp:
                class_num, function_num, char_num, line_num = 0, 0, 0, 0
                for _, ln in enumerate(fp):
                    if ln.lstrip()[:5] == 'class':
                        class_num += 1
                    elif ln.lstrip()[:3] == 'def':
                        function_num += 1

                    char_num += len(ln)
                    line_num += 1
                cur_dic = {
                    'class': class_num,
                    'function': function_num,
                    'line': line_num,
                    'char': char_num
                }
                self.files_summary[file] = cur_dic
                self.table.add_row([self.directory + '/' + file, class_num, function_num, line_num, char_num])



    def pretty_print(self):
                print(self.table)
