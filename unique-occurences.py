# Task: Given a list of numbers arr, return True if each number inside arr occurs uniquely inside arr.

# Conceptual Idea: There is no trick here. But the intuition is to use a dictionary (more or less equivalent to hashmap) that stores the numbers
#                  inside arr as keys and the amount of times that they occur as values. Convert values to a set, and if the length of that set
#                  == length of values in dictionary, then each number in arr occurs uniquely, else the set would filter out duplicate values 
#                  causing its length to be shorter.

# Complexity: Time complexity is O(n) because of the various conversions, arr -> dict, dict.values() -> set, and looping through arr to get the
#             occurences of the numbers. Space complexity is also O(n).
def uniqueOccurrences(arr):
    d = {v: 0 for _, v in enumerate(arr)} 
    for num in arr:
        d[num] += 1

    occurences = d.values()
    arr_set = set(occurences)
    return len(arr_set) == len(occurences)

print(uniqueOccurrences([1,1,2,3,4,-6,7,-1,-6,3,3,2,11,0,0,0,0,9]))
