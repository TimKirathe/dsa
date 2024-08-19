# Task: Given n cities numbered from 0 to n-1 and n-1 directed edges, such that there is only 1 way to go through two cities. Return the minimum number
#       of reorders such that it is possible to get to city 0 from any city

# Conceptual Idea: Start from city 0 and do dfs traversal through the graph. Because edges are directed, create adjacency list using list of edges given.
#                  This will help in doing the dfs correctly. Ensure that current node in traversal as been reordered before visiting it's neighbours
#                  and also mark it as visited so that it is not re-evaluated.

# Complexity: Time complexity is O(n), where n is number of nodes. In worst and best case at most & at least all nodes will be visited.
#             Space complexity is O(n) as well, because recursive stack of function calls will grow with the number of nodes


def minReorder(n, connections):
    adjacency_list = [[] for _ in range(n)]
    visited = [0 for _ in range(n)]
    for conn in connections:
        adjacency_list[conn[0]].append(conn[1])
        adjacency_list[conn[1]].append(-conn[0])

    def dfs(node_from):
        nonlocal visited, adjacency_list
        reorders = 0
        visited[node_from] = 1
        for neighbour in adjacency_list[node_from]:
            if not visited[abs(neighbour)]:
                reorders += dfs(abs(neighbour)) + (neighbour > 0)
        return reorders

    return dfs(0)
