# Task: You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the
#       equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable. You are also given some queries, where
#       queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Conceptual Idea: Frame this as a graph problem, where each variable is a node and each member of values[i] represents an edge between Ai and Bi, or
#                  Bi and Ai. Such that if given query[i] = ("a", "d"), then "a"/"d"=("a"/"b")*("b"/"c")*("c"/"d"). BFS is easier to implement because
#                  DFS would need to account for backtracking in case of going down the wrong route.

# Complexity: Time complexity of BFS O(Q.(|E|.|V|)), because must iterate through each query and for each query in worst case will iterate through
#             the whole graph. So every node will be added to queue and every edge will be iterated through. Space complexity of BFS O(|E|+|V|),
#             because |E|+|V| is the size of the graph in the form of an adjacency list.
import collections


def calcEquation(equations, values, queries):

    adj_list = collections.defaultdict(list)
    for i, eq in enumerate(equations):
        node1, node2 = eq
        adj_list[node1].append((node2, values[i]))
        adj_list[node2].append((node1, 1 / values[i]))

    def bfs(start, end):
        nonlocal adj_list
        if start not in adj_list or end not in adj_list:
            return -1.00000
        q, visited = collections.deque(), set()
        q.append((start, 1))
        visited.add(start)
        while q:
            cur, product = q.popleft()
            if cur == end:
                return product
            for nei, wei in adj_list[cur]:
                if nei not in visited:
                    q.append((nei, wei * product))
                    visited.add(nei)
        return -1.00000

    return [bfs(query[0], query[1]) for query in queries]
