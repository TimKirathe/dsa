# Task: Given an M x N matrix, and a starting point entrance = [row, col], return the shortest number of steps needed to exit the maze - only being
#       allowed to move in the: Up, Down, Left, Right directions - where an exit is defined as an edge without a wall in the maze. Walls are defined as
#       "+" in the maze and empty cells as ".".

# Conceptual Idea: Use BFS to traverse the maze in every direction starting from the entrance until reach the first edge. The initial error I made was
#                  that I thought that the shortest route to the exit could be used by just trying to use a heuristic to pick the best direction to move
#                  in at every stage. This is not necessarily practical for this question an BFS does just fine in doing this, but for each of the 4
#                  directions at once. Think about it like each cell is a node in a tree "rooted" at the entrance, and each cell can have at most 4
#                  children and at least 0. The shortest distance therefore, is between the root node and the first leaf. BFS will ensure that the first
#                  edge I reach is first leaf, because I traverse the tree level by level.

# Complexity: Time complexity is O(H), where H is the height of the graph. In worst case, the graph is a list hence will end up traversing the whole maze.
#             Therefore, time complexity is O(MxN). Space complexity is O(MxN) as well because of the visited matrix which grows with the size of the maze.


from collections import deque


def nearestExit(maze, entrance):
    m, n = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False for _ in range(n)] for _ in range(m)]

    queue = deque()
    queue.append(entrance)
    visited[entrance[0]][entrance[1]] = True
    num_steps = 0
    while queue:
        num_steps += 1
        size = len(queue)
        while size:
            coords = queue.popleft()
            for deltax, deltay in directions:
                x, y = coords[1] + deltax, coords[0] + deltay
                if (
                    (-1 < x < n)
                    and (-1 < y < m)
                    and not visited[y][x]
                    and maze[y][x] == "."
                ):
                    if x == 0 or y == 0 or x == n - 1 or y == m - 1:
                        return num_steps
                    visited[y][x] = True
                    queue.append([y, x])
            size -= 1

    return -1


steps = nearestExit(
    [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2]
)
print(f"num_steps={steps}")
