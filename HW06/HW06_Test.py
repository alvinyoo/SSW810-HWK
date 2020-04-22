"""
Yuchen Yao
HW06 Test
this assignment is going to test the 4 tasks in HW06 .
"""

import unittest
from HW06 import list_copy, list_intersect, list_difference, remove_vowels, check_pwd, DonutQueue


# PART 1 TEST
class ListCopyTest(unittest.TestCase):
    def test_list_copy(self):
        l1 = ['a', 2, 2.22, ['b', 3], {3: {3: 4}}]
        l2 = list_copy(l1)
        self.assertEqual(l1, l2)


# PART 2 TEST
class ListIntersectTest(unittest.TestCase):
    def test_list_intersect(self):
        l1 = [1, 2, 3]
        l2 = [1, 2, 4]
        l3 = [4, 5, 6]
        result1 = list_intersect(l1, l2)
        result2 = list_intersect(l1, l3)
        expect1 = [1, 2]
        expect2 = []
        self.assertEqual(result1, expect1)
        self.assertEqual(result2, expect2)


# PART 3 TEST
class ListDifferenceTest(unittest.TestCase):
    def test_list_difference(self):
        l1 = [1, 2, 3]
        l2 = [1, 2, 4]
        l3 = [4, 5, 6]
        result1 = list_difference(l1, l2)
        result2 = list_difference(l1, l3)
        expect1 = [3]
        expect2 = [1, 2, 3]
        self.assertEqual(result1, expect1)
        self.assertEqual(result2, expect2)


# PART 4 TEST
class RemoveVowelsTest(unittest.TestCase):
    def test_remove_vowels(self):
        s1 = "Amy is my favorite daughter"
        s2 = "Jan is my best friend"
        e1 = "my favorite daughter"
        e2 = "Jan my best friend"
        self.assertEqual(remove_vowels(s1), e1)
        self.assertEqual(remove_vowels(s2), e2)


# PART 5 TEST
class PasswordCheckTest(unittest.TestCase):
    def test_check_pwd(self):
        p1 = "1AaBb"
        p2 = "AaBb"
        p3 = "1Aa"
        p4 = "1aabb"
        p5 = "1AABB"
        p6 = ""
        self.assertTrue(check_pwd(p1))
        self.assertFalse(check_pwd(p2))
        self.assertFalse(check_pwd(p3))
        self.assertFalse(check_pwd(p4))
        self.assertFalse(check_pwd(p5))
        self.assertFalse(check_pwd(p6))


# PART 6 TEST
class DonutQueueTest(unittest.TestCase):
    def test_queue(self):
         dq = DonutQueue()
         self.assertIsNone(dq.next_customer())
         dq.arrive("Sujit", False)
         dq.arrive("Fei", False)
         dq.arrive("Prof JR", True)
         self.assertEqual(dq.waiting(), "Prof JR, Sujit, Fei")
         dq.arrive("Nanda", True)
         self.assertEqual(dq.waiting(), "Prof JR, Nanda, Sujit, Fei")
         self.assertEqual(dq.next_customer(), "Prof JR")
         self.assertEqual(dq.next_customer(), "Nanda")
         self.assertEqual(dq.next_customer(), "Sujit")
         self.assertEqual(dq.waiting(), "Fei")
         self.assertEqual(dq.next_customer(), "Fei")
         self.assertIsNone(dq.next_customer())
