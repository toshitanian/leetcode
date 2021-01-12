# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        ind = k - 1
        node_list = []
        node = head
        while True:
            node_list.append(node)
            if node.next is None:
                break
            node = node.next
        print(node_list)

        first = node_list[ind]
        first_val = first.val
        second = node_list[len(node_list) -1 - ind]
        second_val = second.val
        print(first_val)
        print(second_val)

        first.val = second_val
        second.val = first_val
        return head

def list_to_linkedlist(l):
    prev = None
    head_node = None
    for e in l:
        n = ListNode(e)
        if prev is None:
            head_node = n
        else:
            prev.next = n
        prev = n
    return head_node

def linkedlist_to_list(head_node):
    l = []
    node = head_node
    while True:
        l.append(node.val)
        if node.next is None:
            break
        node = node.next
    return l

def t():
    s = Solution()
    # Input: head = [1,2,3,4,5], k = 2
    #  Output: [1,4,3,2,5]
    l = [1,2,3,4,5]
    k = 2
    head_node = list_to_linkedlist(l)
    print(linkedlist_to_list(head_node))
#    print(ll)
    h = s.swapNodes(head_node, k)
    print(linkedlist_to_list(h))


t()