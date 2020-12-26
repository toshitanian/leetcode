from typing import NewType
# For just avoid type error
ListNode = NewType('ListNode', list)

def linked_list_to_sorted_list(l):
    input_list = []
    n = l
    while n is not None:
        input_list.append(n.val)
        n = n.next
    input_list.reverse()
    return input_list

def number_list_to_number(l):
    l.reverse()
    total = 0
    for i, n in enumerate(l):
        base = 10 ** i
        total += n * base
    return total

def number_to_reversed_linked_list(l):
    # Not clean solution
    num_list = [int(_) for _ in str(l)]

    num_list.reverse()

    nodes = [ListNode(_) for _ in num_list]

    for i, n in enumerate(nodes):
        if i + 1 < len(nodes):
            n.next = nodes[i+1]

    return nodes[0]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        """
        list_1 = linked_list_to_sorted_list(l1)
        list_2 = linked_list_to_sorted_list(l2)
        num_1 = number_list_to_number(list_1)
        num_2 = number_list_to_number(list_2)
        total = num_1 + num_2
        result_reversed_list = number_to_reversed_linked_list(total)
        return result_reversed_list

def t():
    r = number_list_to_number([2, 4, 5])
    r = number_to_reversed_linked_list(678)
    print(r)


t()