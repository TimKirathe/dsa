# Task: You have an array of arrays called 'rooms'. Each array within rooms represents a room which holds the keys for other rooms that can be
#       visited from it. Return true if all the rooms can be visited, false otherwise.

# Conceptual Idea: Because the key numbers within different rooms can repeat themselves, need a dictionary to store keys of rooms which have been visited
#                  If already visited, no need to do so again. But, need a recursive function to check each room for the keys they have available. If
#                  length of visited rooms == length of original list of rooms, all rooms have been visited, hence can return true, else false.

# Complexity: Time complexity is O(R + K), where R = Rooms & Keys = Total num of unique keys, because evaluating whether a room has been searched
#             is O(N) and in that case, the room is never visited again. Therefore it's not O(N*K), but O(N + K). Space complexity is O(N), because
#             there are at most N calls to the recursive stack.


def can_visit_all_rooms(rooms):
    searched_rooms = {0: True}
    N = len(rooms)

    def find_keys(current_key):  # O(N)
        keys = rooms[current_key]
        for key in keys:  # O(K)
            if key in searched_rooms:  # O(1)
                continue
            searched_rooms[key] = True
            find_keys(key)

    find_keys(0)
    return len(searched_rooms.keys()) == N


test_rooms = [[2, 1], [3], [2], [1], [5, 6], [4], [0]]
print(can_visit_all_rooms(test_rooms))
