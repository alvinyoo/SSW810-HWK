"""
Created on Thr Oct 16 2019

@author: Lin Zheng

HW07 implementation file layout template
"""

from collections import defaultdict, Counter

def anagram_lst(str1, str2):
    """  return the boolean value of whether str1 and str2 are anagrams using list  """
    return sorted(str1.lower()) == sorted(str2.lower())

def anagrams_dd(str1, str2):
    """  return the boolean value of whether str1 and str2 are anagrams using defaultdict  """
    dd = defaultdict(int)

    for c in str1:
        dd[c] += 1

    for c in str2:
        if c in dd:
            dd[c] -= 1
        else:
            return False 

    return not any(dd.values()) 
    

def anagrams_cntr(str1, str2):
    """  return the boolean value of whether str1 and str2 are anagrams using counter  """
    return Counter(str1.lower()) == Counter(str2.lower())

def covers_alphabet(sentence):
    """  return the boolean value of whether sentence includes at least one instance
         of every character in the alphabet using set  
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return all([ c in set(sentence.lower()) for c in alphabet ])
    #return set(sentence.lower()) >= set('abcdefghijklmnopqrstuvwxyz')
    
def book_index(words):
    """  return a book index  """
    dd = defaultdict(lambda: set())
    for wd, pg in sorted(words):
        dd[wd].add(pg)
    
    return [ [key, list(value)] for key, value in dd.items() ]

    
    
