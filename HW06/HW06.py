"""
Yuchen Yao
HW06
this homework contained 4 tasks
"""


from typing import List, Any, Optional


# PART 1
def list_copy(l: List[Any]) -> List[Any]:
    """ takes a list as a parameter and returns a copy of the list """
    # my_list: List[Any] = []
    # for i in l:
    #     my_list.append(i)
    # return my_list

    return [i for i in l]


# PART 2
def list_intersect(l1: List[Any], l2: List[Any]) -> List[Any]:
    """ takes two lists as  parameters and returns a new list with the values that are included in both lists """
    # my_list = []
    # for i in l1:
    #     if i in l2:
    #         my_list.append(i)
    # return my_list

    return [i for i in l1 if i in l2]


# PART 3
def list_difference(l1: List[Any], l2: List[Any]) -> List[Any]:
    """ takes two lists as  parameters and returns a new list with the values that are  in l1, but NOT in l2 """
    # my_list = []
    # for i in l1:
    #     if i not in l2:
    #         my_list.append(i)
    # return my_list

    return [i for i in l1 if i not in l2]


# PART 4
def remove_vowels(string: str) -> str:
    """ given a string, returns a new string that includes only the words that do NOT begin with vowels """
    # vowels = 'aeiouAEIOU'
    # my_list = string.split()
    # new_list = []
    # for x in my_list:
    #     if x[0] not in vowels:
    #         new_list.append(x)
    # return ' '.join(new_list)

    return ' '.join([i for i in string.split() if i[0] not in 'aeiouAEIOU'])
    # return ' '.join([i for i in string.split() if i。lower[0] not in 'aeiou'])


# PART 5
def check_pwd(password: str) -> bool:
    """
    returns True if all conditions below are satisfied:
        The password includes at least two upper case characters
        The password includes at least one lower case characters
        The password starts with at least one digit
    """
    # if not password[0].isdigit():
    #     return False
    #
    # upper_cnt = 0
    # lower_cnt = 0
    #
    # for x in password:
    #     if 65 <= ord(x) <= 90:
    #         upper_cnt += 1
    #     if 97 <= ord(x) <= 122:
    #         lower_cnt += 1
    #
    # if upper_cnt < 2 or lower_cnt < 1:
    #     return False
    #
    # return True

    # return password[0].isdigit() and len(list(filter(lambda i: 65 <= ord(i) <= 90, password))) >= 2 \
    #        and len(list(filter(lambda i: 97 <= ord(i) <= 122, password))) >= 1

    """solution 1"""
    # return password[0].isdigit() \
    #     and len([ch for ch in password if ch.isupper()]) >= 2 \
    #     and any([ch.islower() for ch in password])

    """solution 2"""
    return len(password) >= 4 \
        and sum([1 for c in password if c.isupper()]) >= 2 \
        and sum([1 for c in password if c.islower()]) >= 1 \
        and password[0].isdigit()


# PART 6
class DonutQueue:
    """ tracks customers as they arrive at the donut shop """
    def __init__(self) -> None:
        # self.queue = [('name1', True), ('name2', False)]
        self.vip_queue: List = []
        self.standard_queue: List = []

    def arrive(self, name: str, vip: bool) -> None:
        """ to note that a customer arrived """
        if vip:
            self.vip_queue.append(name)
        else:
            self.standard_queue.append(name)

        # if vip:
        #     index: Optional[int] = None
        #     for i in range(len(self.queue) - 1, -1, -1):
        #         if self.queue[i][1]:
        #             index = i
        #             break
        #
        #     if index is not None:
        #         self.queue.insert(index + 1, (name, vip))
        #     else:
        #         self.queue.insert(0, (name, vip))
        # else:
        #     self.queue.append((name, vip))

    def next_customer(self) -> Optional[str]:
        """
        returns the name of the next customer to be served where all priority customers are served in the order
        they arrived before any non-priority customer
        """
        # return self.queue.pop(0)[0] if self.queue else None

        if self.vip_queue:
            return self.vip_queue.pop(0)
        elif self.standard_queue:
            return self.standard_queue.pop(0)
        else:
            return None

    def waiting(self) -> Optional[str]:
        """
        returns a comma separated string with the names of the customers waiting in the order they will be served
        or None if there are no customers waiting
        """
        waiting_list: List[str] = self.vip_queue + self.standard_queue
        return ', '.join(waiting_list) if waiting_list else None
        # tmp: List[str] = [x[0] for x in self.queue]
        # return ', '.join(tmp) if tmp else None
