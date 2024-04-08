# Task: Given nodes of a linked list consisting of a value and pointer to next node, delete the middle node of the linked list.

# Conceptual Idea: Use a 'fast' pointer and a 'slow' pointer. Have the 'fast' pointer move 2 units ahead & slow pointer move one unit ahead during loop
#                  iteration. Logic is that by the time 'fast' pointer has reached end of list, slow pointer will be at the middle of the list because
#                  fast is moving 2x faster than slow. During execution of loop, keep variable 'prev' that stores node that comes before one pointed by
#                  slow. When reach end of list, change pointer of prev.next to slow.next, effectively skipping over middle node at slow.

# Complexity: Time complexity is O(n), because need to iterate through whole LinkedList. Space complexity is O(1), because size of fast, slow and prev
#             variables remains constant throughout loop irrespective of size of LinkedList.


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

    if slow == fast:
        head = head.next
    else:
        prev.next = slow.next
    return head


lNode = ListNode(1, ListNode(2, None))

print(deleteMiddle(lNode))
