"""
Created on Thr Oct 7 2019

@author: Lin Zheng

HW06 implementation file layout template
"""

def list_copy(l):
    """  takes a list as a parameter and returns a copy of the list using a list comprehension """
    return [ item for item in l ]

def list_intersect(l1, l2):
    """  takes two lists as parameters and returns a new list with the values included in both lists """
    return [ item for item in l1 if item in l2 ]
    
def list_difference(l1, l2):
    """   takes two lists as  parameters and returns a new list with the different values """
    return [ item for item in l1 if item not in l2 ]

def remove_vowels(string):
    """ returns a copy of the string with no vowels """
    return ''.join([ item for item in string if item.lower() not in 'aeiou'])

def check_pwd(password):
    """ takes a string as a parameter and returns a boolean value showing whether it meets requirements """
    return any([ item.islower() for item in password ]) \
           and any([ item.isupper() for item in password ]) \
           and password[-1].isdigit()

def insertion_sort(l):
    """ returns a copy of the argument sorted using a list and the insertion sort algorithm """
    result = list()
    for item in l:
        for offset, c in enumerate(result):
            if item <= c:
                result.insert(offset, item)
                break         
        else:
            result.append(item)

    return result

def insertion_sort(l):
    """ returns a copy of the argument sorted using a list and the insertion sort algorithm """
    result = list()
    for item in l:
        offset = 0
        while offset < len(result) and result[offset] < item:
            offset += 1

        result.insert(offset, item)

    return result