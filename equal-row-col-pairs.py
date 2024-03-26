# Task: Given an NxN matrix, return the number of equal pairs. Equal pairs consist of rows and columns that contain the same values in the same order.

# Conceptual Idea: Hash each row and column in the grid. Given that you use a good hash function, there should be little to no conflicts and the
#                  function will be deterministic, hence getting the same hash value when the arrays are the same. Keep count of the number of 
#                  arrays (rows OR columns) that have the same value. These will be the ones that represent equal pairs.

# Complexity: Time complexity is O(n^2), because of the inner for loop that is required to create the columns. This is due to the notation of 2-dimensional
#             arrays in python. The process of hashing the arrays and checking if the hash values are the same is contant due to the O(1) beahviour of
#             the hash function. This saves the time complexity from being O(n^3) which would happen when checking each values equality one-by-one in the
#             grid. The Space complexity is O(n) because the size of the Counter object would be 2N, where N represents the num of rows & columns,
#             in the worst-case when there are no equal pairs.

import collections

def equalPairs(grid):
    element_counter = collections.Counter()
    N = len(grid)
    equal_pairs = 0
    for i in range(N):
        # keys will be tuples because they are hashable in python
        element_counter[tuple(grid[i])] += 1
        
    for i in range(N):
        column = []
        for j in range(N):
            column.append(grid[j][i])
        # will add the value already held in the counter object if the column is equal to any of the rows held there. Otherwise will add 0 if the
        # value does not already exist.
        equal_pairs += element_counter[tuple(column)]
    return equal_pairs

print(equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
