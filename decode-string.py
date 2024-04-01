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

print(decodeString('2[3[aaa2[bght7[g4[5[b]]]]]]'))
