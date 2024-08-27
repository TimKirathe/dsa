# Task: You are given an m x n grid where each cell can have one of three values:
#         - 0 representing an empty cell,
#         - 1 representing a fresh orange, or
#         - 2 representing a rotten orange.

#         Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. Return the minimum number of minutes that
#         must elapse until no cell has a fresh orange. If this is impossible, return -1

# Conceptual Idea: Use BFS. But, the trick here is that you should start the traversal with all initial rotten oranges in the queue and then do BFS level
#                  by level from there, turning every adjacent fresh orange to a rotten one, and adding it to the queue. Keep a count of how many fresh
#                  oranges there were at the start and check to see if all have been turned rotten, cause there might be a fresh orange without any
#                  adjacent orange which even after the BFS doesn't get turned into a rotten orange.

# Complexity: Time complexity is O(MxN), where M is the num of rows, and N the num of columns in the grid. This is because of the need to iterate through
#             grid intially, to add the rotten oranges to the queue and count the number of fresh oranges. Space complexity is O(MxN) as well because of
#             the visited matrix needed to keep track of which nodes are & aren't visited.

from collections import deque


def orangesRotting(grid):
    fresh_oranges = 0
    q = deque()
    M, N = len(grid), len(grid[0])
    visited = [[False for _ in range(N)] for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 2:
                q.append((i, j))
                visited[i][j] = True
            elif grid[i][j] == 1:
                fresh_oranges += 1
    if fresh_oranges == 0:
        return 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    num_minutes = 0
    corrupted_oranges = 0
    while q:
        size = len(q)
        while size:
            row, col = q.popleft()
            for x, y in directions:
                deltay, deltax = row + y, col + x
                if -1 < deltay < M and -1 < deltax < N and not visited[deltay][deltax]:
                    if grid[deltay][deltax] == 1:
                        corrupted_oranges += 1
                        grid[deltay][deltax] = 2
                        q.append((deltay, deltax))
                    visited[deltay][deltax] = True
            size -= 1
        if q:
            num_minutes += 1
    if fresh_oranges - corrupted_oranges == 0:
        return num_minutes
    return -1


minutes = orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
print(minutes)
