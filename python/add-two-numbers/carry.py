# I'm solving this after watching solutions.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        """
        first_node = ListNode()
        current_node = first_node
        carry = 0

        node_1 = l1
        node_2 = l2
        while True:
            n1 = node_1.val if node_1 is not None else 0
            n2 = node_2.val if node_2 is not None else 0
            _sum = n1 + n2 + carry

            if _sum > 9:
                carry = 1
            else:
                carry = 0
            node_num = _sum % 10
            current_node.val = node_num
            if node_1 is not None and node_1.next is not None:
                node_1 = node_1.next
            else:
                # node.next is None or node is None
                node_1 = None

            if node_2 is not None and node_2.next is not None:
                node_2 = node_2.next
            else:
                node_2 = None

            if node_1 is None and node_2 is None:
                if carry > 0:
                    next_node = ListNode(carry)
                    current_node.next = next_node
                break

            next_node = ListNode()
            current_node.next = next_node
            current_node = next_node

        return first_node

def number_to_reversed_linked_list(n):
    # Not clean solution
    num_list = [int(_) for _ in str(n)]

    num_list.reverse()

    nodes = [ListNode(_) for _ in num_list]

    for i, n in enumerate(nodes):
        if i + 1 < len(nodes):
            n.next = nodes[i+1]

    return nodes[0]

def linked_list_to_number(l):
    n = l
    total = 0
    index = 0
    while n is not None:
        total += n.val * 10 ** (index)
        n = n.next
        index += 1
    return total


def t():
    l1 = number_to_reversed_linked_list(9999999)
    l2 = number_to_reversed_linked_list(9999)
    s = Solution()
    r = s.addTwoNumbers(l1, l2)
    print(linked_list_to_number(r))

t()
