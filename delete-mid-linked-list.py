# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteMiddle(head):
    slow, fast, prev = head, head, None
    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    prev.next = slow.next
    return head


lNode = ListNode(1, ListNode(2, None))

print(deleteMiddle(lNode))
