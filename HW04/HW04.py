"""
Yuchen Yao
HW04
this is contained 5 tasks
"""

from typing import Any, Optional, Sequence, Iterator, Tuple


# PART 1
def count_vowels(seq: str) -> int:
    """ return the number of vowels in the string s """
    count: int = 0
    seq = seq.lower()
    for i in seq:
        if i in "aeiou":
            count += 1
    return count


# PART 2
def find_last(target: Any, seq: Sequence[Any]) -> Optional[int]:
    """ return the offset from 0 of the last occurrence of target in seq """
    index: Optional[int] = None
    for offset, i in enumerate(seq):
        if i == target:
            index = offset
    return index


# PART 4
def my_enumerate(seq: Sequence[Any], start=0) -> Iterator[Tuple[int, Any]]:
    """
        emulate the behavior of Python's built in enumerate() function.
        For each call, return a tuple with the offset from 0 and the next item
    """
    offset: int = start
    value: Any
    for value in seq:
        yield offset, value
        offset += 1


def my_enumerate_sarita(seq: Sequence[Any]) -> Iterator[Any]:
    yield from zip(range(len(seq)), seq)


def my_numerate_yinhui(seq: Sequence[Any]) -> Iterator[Any]:
    for i in range(len(seq)):
        yield i, seq[i]
