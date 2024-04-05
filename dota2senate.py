# Task: Given a string consisting of characters that are either 'R' or 'D', simulate a round of voting in the senate such that any senator belonging to
#       parties R or D, ban another senator from voting, or, if there are no more remaining senators in the opposite party, announce the victory of
#       their party. The voting is to be simulated in a left to right manner, until there are no more remaining members of one particular party. Note
#       that one party is guaranteed to win. You are also to assume that each member of the senate always votes optimally.

# Conceptual Idea: The key to understanding this question is realising that the way the task is worded is very shrewd. Firstly, voting is simulated
#                  in a right-left manner, meaning that for the senators to vote optimally, they must always ban the senator from the opposite party who
#                  is closest to them on the right. Understanding this, the trick lies in being able to simulate the 'loop around' that would occur in
#                  the case that the first-round of voting does not produce a solution as to who the winner is. To do this, every time the i'th senator
#                  bans another opponent, we must 'move' them len(senate) + senate[i] positions to the right. In the case where a voting j'th senator has
#                  no more positions to the right that he can ban, this 'move' will mean that senator[j] will ban the senator from the opposite party who
#                  least recently voted. In reality the senators are not moved, rather, their indices are changed to reflect this. See the code below as
#                  to why the Queue data structure is best for this kind of solution.

# Complexity: Time complexity is O(n+k), where n = len(senate) & k = number of pops from the 2 Queues. Space complexity is the same, because the size of
#             the 2 Queues combined is at most n.

from collections import deque


def predictPartyVictory(senate):
    (
        RQ,
        DQ,
    ) = (
        deque(),
        deque(),
    )
    N = len(senate)
    for i in range(len(senate)):
        if senate[i] == "R":
            RQ.append(i)
        else:
            DQ.append(i)

    # To simulate voting, need to compare indices from left-right of each Queue and append the necessary indices back to the end of the Queue to
    # represent 'looping again' through the voting round. Hence need to pop from left and append to right. Python's deque is perfect for this.
    while RQ and DQ:
        R = RQ.popleft()
        D = DQ.popleft()

        if R < D:
            RQ.append(R + N)
            # RQ.append(D + N) # Same as above, but basically done to represent the fact that the guy with the lower index, bans the guy with the higher index, then 'takes' his place in the queue. This doesn't affect the solution though.
        else:
            DQ.append(D + N)
            # DQ.append(R + N) # Same as above, but basically done to represent the fact that the guy with the lower index, bans the guy with the higher index, then 'takes' his place in the queue. This doesn't affect the solution though.
    return "Radiant" if RQ else "Dire"


print(predictPartyVictory("RDDRRDDDR"))
