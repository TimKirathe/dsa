# Task: Given a string s, remove all *'s from the string including the character to the left of each *.

# Conceptual Idea: To keep track of the formatted string with removed *'s, use a stack. Iterate through the string & append to the stack if the
#                  if the current char is not a *, if it is, pop the character on the top of the stack because it will be the leftmost char of the
#                  *. Don't push the * to the stack

# Complexity: Time complexity is O(n) because of iterating through the string. The push & pop operations to the stack are done in constant time.
#             Space complexity is O(n) as well because in the worst case, the stack would be the same size as s if there are no *
def removeStars(s):
    s_stack = []
    for char in s:
        if char == '*':
            s_stack and s_stack.pop()
        else:
            s_stack.append(char)
    return ''.join(s_stack)   

print(removeStars('lasdklf**sadkjf*jfajsdkfj*ksjdfkljaslfj****jsdfjklasdjfkj*'))
