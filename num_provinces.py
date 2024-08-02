# Task: You have an adjacency matrix isConnected whose rows and columns represent cities, and isConnected[i][j] means that city i is connected to city j.
#       If city i is connected directly with city j, and city j is connected directly with city k, then city a is connected indirectly with city k, and
#       they form a 'province'. Return the number of provinces

# Conceptual Idea: This problem is one of disjoint sets. Use a Union-Find data structure. If 2 cities are connected, merge them. Count the number of
#                  provinces at the end. Provinces correspond to the number of disjoint sets.

# Complexity:


# This implementation uses indexes to represent nodes and the values at those indexes to represent the nodes' parents.
class UF:
    def __init__(self, N):
        self.nodes = [i for i in range(N)]
        self.sizes = [1 for _ in range(N)]
        self.length = N

    def find(self, x):
        if self.nodes[x] == x:
            return x
        return self.find(self.nodes[x])

    def merge(self, x, y):
        if self.nodes[x] == self.nodes[y]:
            return
        elif self.sizes[x] < self.sizes[y]:
            self.nodes[x] = y
            self.sizes[y] += self.sizes[
                x
            ]  # because a child/children have been added to y above, so y's size increases
        else:
            self.nodes[y] = x
            self.sizes[x] += self.sizes[
                y
            ]  # because a child/children have been added to y above, so y's size increases

    def check_provinces(self):
        provinces = 0
        for i in range(self.length):
            if (
                self.nodes[i] == i
            ):  # because if self.nodes[i] == i, then i is its own parent showing that it represents a province. Other nodes that have a parent different from themselves are part of a disjoint set, hence don't represent a province.
                provinces += 1
        return provinces


def findCircleNum(isConnected):
    N = len(isConnected)
    union_find = UF(N)
    for i in range(N):
        for j in range(
            i + 1, N
        ):  # Don't need to iterate through half of the matrix including positions where i==j, because those are just repeat values.
            if isConnected[i][j]:
                node_i, node_j = union_find.find(i), union_find.find(j)
                union_find.merge(node_i, node_j)

    return union_find.check_provinces()


provinces = findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
print(provinces)
