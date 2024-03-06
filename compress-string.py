# Task: Compress a string that is converted into a list of characters. Do this by replacing each sequence of identical characters in the list with the character that repeats and the number of times that it does. Each digit that makes up the number of times it repeats should be added individually, not as a whole number.
# Conceptual idea: Iterate through the list using 2 pointers i and j. i keeps track of the iterations through the list, and j keeps track of the position(s) to replace repeating characters behind the one at position i, with the character that repeats and the number of times it repeats.
# Complexity: It has a tight-bound of O(n) because the problem of finding out how many of each character there is in a list involves iterating through the whole list at least once. This solution will also only iterate through the list at most once. 
def compress(chars) :
    if len(chars) == 1:
            return 1
    length = len(chars)
    char_pointer, count_pointer = 0, 0
    while char_pointer < length:
        count = 1
        while char_pointer < length - 1 and chars[char_pointer] == chars[char_pointer + 1]:
            count += 1
            char_pointer += 1
        
        chars[count_pointer] = chars[char_pointer]
        count_pointer += 1

        if count > 1:
            for digit in str(count):
                chars[count_pointer] = digit
                count_pointer += 1

        char_pointer += 1
    # Return the length of the newly formatted list.
    return count_pointer

chars_list = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']

print(compress(chars_list))
print(chars_list) 