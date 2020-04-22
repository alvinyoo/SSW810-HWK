"""
Yuchen Yao
HW05
this homework contained 4 tasks
"""


from typing import Iterator, IO


# Part 1
def reverse(s: str) -> str:
    """ this function takes a string as an argument and returns a new string which is the reverse of the argument """
    my_list: list = []
    i: int = len(s)

    while i > 0:
        i -= 1
        my_list.append(s[i])
    result: str = "".join(my_list)
    return result


def reverse2(s):
    rev = ""
    for i in s:
        rev = i + rev
    return rev


def reverse3(s):
    rev = ""
    for index in range(len(s)):
        rev = s[index] + rev
        return rev

# Part 2
def substring(target: str, string: str) -> int:
    """
    returns the offset from the beginning of  string s where target occurs in s
    return -1 if target is not a substring in s
    """
    lt: int = len(target)
    offset: int = 0
    i: int

    if target in string:
        while string[offset:lt] != target:
            lt += 1
            offset += 1
        return offset

    else:
        return -1


def substring2(target, string):
    target_len = len(target)
    for i in range(len(string)-target_len+1):
        if string[i + target_len] == target:
            return i
    return -1


# Part 3
def find_second(target: str, string: str) -> int:
    """
    returns the offset of the second occurrence of s1 in s2
    return -1 if s1 does not occur twice in s2
    """
    return string.find(target, string.find(target) + 1) if string.find(target) != -1 else -1
    # lt: int = len(target)
    # offset: int = 0
    # i: int
    #
    # if target in string:
    #     while string[offset:lt] != target:
    #         lt += 1
    #         offset += 1
    #
    #     offset += 1
    #     lt += 1
    #     new_string = string[offset:]
    #
    #     if target in new_string:
    #         while string[offset:lt] != target:
    #             lt += 1
    #             offset += 1
    #         return offset
    #
    #     else:
    #         return -1
    #
    # else:
    #     return -1


# Part 4
def get_lines(path: str) -> Iterator[str]:
    line: str
    try:
        fp: IO = open(path)
    except FileNotFoundError:
        raise FileExistsError(f"Can't find '{path}'")
    else:
        with fp:
            for line in fp:
                line = line.strip('\n')

                if not line:
                    yield line
                    continue

                while line[-1] == '\\':
                    line = line[:-1] + fp.readline().strip('\n')
                    # line = line[:-1] + next(fp).rstrip('\n')

                if '#' in line:
                    if line[0] != '#':
                        yield line[:line.index('#')]

                else:
                    yield line
