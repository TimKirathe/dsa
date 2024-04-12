# Task: Given a linked list head, return a linked list such that the odd & even nodes are grouped together. Odd first, then even. The odd indices start
#        at the first index.

# Conceptual Idea: Use 2 pointers. One 'odd' starting at head that will point to the odd indices & another 'even' starting at head.next, that will point
#                  to to the even indices. At each iteration of loop, update odd.next to odd.next.next & even to even.next.next. Keep original pointer
#                  of even & make last odd.next pointer point to it


# Complexity: Time complexity O(n) because need to iterate through whole linked list. Space complexity O(1) because size of variables remains same
#             irregardless of size of head.
def oddEvenList(head):
    if head == None:
        return head
    even, even_start, odd = head.next, head.next, head
    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
    odd.next = even_start
    return head
