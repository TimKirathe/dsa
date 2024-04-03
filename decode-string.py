# Task: Given a string containing english characters, [], and digits (0-9) return the decoded string such that the [] and digits are removed, & the
#       characters encased within brackets are repeated n times, where n is a digit next to the [ bracket in the string

# Conceptual Idea: Use a stack. Iterate through the string and append to the stack until you reach a ]. When this happens, pop from the stack
#                  and stored the popped characters to a substring until reach the first digit. Pop all digits to get the full number before the [ and
#                  and then transform this number into an int n, to repeat the substring n times. Finally, add the substring to the stack. Work this
#                  solution out and see that it simulates recursion.

# Complexity: Time complexity is O(n) in worst case because need to iterate through whole string, & process of popping from stack could potentially go
#             through whole stack before being appended after multiplication. Space complexity is O(n), because the stack could grow to be size of string
#             in worst case where there is only one sequence of [].


def decodeString(s):
    stack = []
    for i in range(len(s)):
        if s[i] != "]":
            stack.append(s[i])
        else:
            sub = ""
            while stack[-1] != "[":
                sub = stack.pop() + sub
            stack.pop()
            factor = ""
            while stack and stack[-1].isdigit():
                factor = stack.pop() + factor
            stack.append(sub * int(factor))
    return "".join(stack)


print(decodeString("2[3[aaa2[bght7[g4[5[b]]]]]]"))
