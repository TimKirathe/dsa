# Task: Given a linked list head, e.g. 1->2->3->4->5, reverse the pointers such that head is 5->4->3->2->1

# Conceptual Idea: Use 2 pointers. But one 'previous' starts before head & other 'current' starts at head. Incrementally change value of current.next to previous till reach end of list. Use intermediary
#                  variable to preserve value of current when doing current.next = previous, otherwise will lose rest of list during iteration.

# Complexity: Time complexity is O(n) because need to iterate through whole of linked list. Space complexity is O(1), because size of variables remains the same irregardless of size of head


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    previous, current = None, head
    while current:
        temp = current.next
        current.next = previous
        previous = current
        current = temp
    return previous


llist = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
llist = reverseList(llist)

formatted_llist = []
while llist:
    formatted_llist.append(llist.val)
    llist = llist.next

print(formatted_llist)
