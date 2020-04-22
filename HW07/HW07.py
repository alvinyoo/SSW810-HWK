"""
Yuchen Yao
HW07
this homework contained 3 tasks
"""

from typing import List, Tuple, DefaultDict, Any
from collections import Counter, defaultdict
import typing


# PART 1
# PART 1.1
def anagram_lst(str1: str, str2: str) -> bool:
    """ return True if str1 and str2 are anagrams, False if not """
    return sorted(str1) == sorted(str2)


# PART 1.2
def anagram_dd(str1: str, str2: str) -> bool:
    """ return True if str1 and str2 are anagrams, False if not """
    dd: DefaultDict[str, int] = defaultdict(int)
    for i in str1:
        dd[i] += 1

    for i in str2:
        if i in dd:
            dd[i] -= 1
        else:
            return False

    return not any(dd.values())  # any dd.value is not other than 0


def anagram_dd2(str1, str2):
    dd = defaultdict(int)
    for i in str1:
        dd[i] += 1

    for i in str2:
        dd[i] -= 1

    return not any(dd.values())
#   for i in dd.values():
#       if i != 0:
#           return False
#   return True


# PARt 1.3
def anagram_cntr(str1: str, str2: str) -> bool:
    """ return True if str1 and str2 are anagrams, False if not """
    c1: typing.Counter = Counter(str1)
    c2: typing.Counter = Counter(str2)
    if len(c1.keys()) != len(c2.keys()):
        return False

    for key in c1.keys():
        if c1[key] != c2[key]:
            return False

    return True


def anagram_cntr2(str1, str2):
    return Counter(str1.lower()) == Counter(str2.lower())


def anagram_cntr3(str1, str2):
    result = Counter(str1.lower())
    result.subtract(str2.lower())
    return all(cnt == 0 for cnt in result.values())


# PART 2
def covers_alphabet(sentence: str) -> bool:
    """
    returns true if sentence includes at least one instance
    of every character in the alphabet or False using only Python sets
    """
    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    s: str = sentence.lower()
    for c in alphabet:
        if c not in s:
            return False

    return True


def covers_alphabet2(sentence):
    return set(sentence.lower()) >= set("abcdefghijklmnopqrstuvwxyz")


# PART 3
def web_analyzer(weblogs: List[Tuple[str, str]]) -> List[Tuple[str, List[str]]]:
        """
        create a summary of the weblogs with each distinct site
        and a sorted list of names of distinct people who visited that site
        """
        weblogs = set(weblogs)
        summary: DefaultDict[Any, List] = defaultdict(list)
        name: str
        web: str
        for name, web in weblogs:
            summary[web].append(name)

        for key in summary:
            lst = summary[key]
            lst.sort()
            summary[key] = lst

        res = []
        for key in summary:
            lst = summary[key]
            tup = (key, lst)
            res.append(tup)

        res.sort(key=lambda item: item[0])

        return res


def web_analyzer2(weblogs):
    summary = defaultdict(set)

    for name, site in weblogs:
        summary[site].add(name)

    return [(site, sorted(list(summary[site]))) for site in sorted(summary.keys())]
#   return sorted([(site, sorted(list(summary[site]))) for site in summary.keys()])
