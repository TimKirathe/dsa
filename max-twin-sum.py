# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pairSum(head):
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    previous = None
    while slow:
        temp = slow.next
        slow.next = previous
        previous = slow
        slow = temp

    max_twin_sum = 0
    while previous:
        s = head.val + previous.val
        max_twin_sum = max(max_twin_sum, s)
        head = head.next
        previous = previous.next
    return max_twin_sum
