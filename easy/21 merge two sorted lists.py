"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def display(node):
    elem = []
    cur = node
    while cur.next:
        elem.append(cur.val)
        cur = cur.next
    print(elem)

def iteration(l1, l2):
    dummy = ListNode(-1)
    cur = dummy

    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next

    if l1:
        cur.next = l1
    else:
        cur.next = l2
    return dummy.next

def recursion(l1, l2):
    if not l1:
        return l2
    elif not l2:
        return l1
    if l1.val < l2.val:
        l1.next = recursion(l1.next, l2)
        return l1
    else:
        l2.next = recursion(l2.next, l1)
        return l2


# if __name__ =='__main__':
