# Task: Given 2 integer lists nums1 & nums2, return answer1 (the list of all integers in nums1 and not in nums2) & answer2 (list of all integers
#       in nums2 and not in nums1)

# Conceptual Idea: Because we can't avoid checking if each integer in both arrays is in the other, we need efficiency of access to speed up performance
#                  therefore, convert nums1, nums2, answer1 & answer2 to hashsets which have O(1) read and delete time. They have added benefit that they
#                  do not allow duplicate values. This means that when checking if integer i exists in either set, that memory access would be O(1) time.

# Complexity: Time complexity is O(n + m), where n is size of nums1 & m is size of nums2. This is because I iterate through each list once. Within for 
#             loop when checking if integer exists in list, the O(1) access time makes overall complexity O((n+m)*1) instead of O((n+m)*nm) If I were
#             to leave nums1 & nums2 as lists. Space complexity is O(n + m)

def findDifference(nums1, nums2):
    answer1, answer2 = set(), set()
    set1, set2 = set(nums1), set(nums2)

    for i in range(len(nums1)):
        if nums1[i] not in nums2:
            answer1.add(nums1[i])

    for j in range(len(nums2)):
        if nums2[j] not in nums1:
            answer2.add(nums2[j])

    answer = [list(answer1), list(answer2)]
    return answer

print(findDifference([1,2,3], [2,4,6]))
