# Task: Given a list of integers that represent asteroids, return the list of asteroids that have removed all those involved in a collision. Asteroids
#       with a -ve sign move in left direction, w/ +ve sign move in right direction. Two asteroids only collide if they are moving in opposite directions.
#       The asteroids move at same speed, therefore it is impossible for 2 moving in same direction to collide. When asteroids collide, the one with a
#       bigger magnitude remains, smaller magnitude destroyed.

# Conceptual Idea: Use a stack, because evaluating collisions of asteroids in the list involves looking at the list from left-right & checking whether 
#                  adjacent ones collide. This involves a lot of appending to, and removing from, the position in the list that has been most recently 
#                  iterated through during the loop. The trick is that a collision only happens when the asteroid at top of stack +ve, & current one in
#                  loop is -ve. In this case, their summation determines which one is destroyed. If +ve, ignore current one, if -ve, pop from stack & add 
#                  current one (repeat until condition False), if same, pop from stack & ignore current one.

# Complexity: Time complexity is O(n+m), because of the inner while loop. n represents length of asteroids, m represents the number of pops & appends to 
#             the stack in the inner while loop. Because popping and appending are O(1) operations, the time complexity remains O(n). Space complexity is
#             O(n) as well because in worst case the stack is as big as the length, n of asteroids.
def asteroidCollision(asteroids):
    stack = []
    for asteroid in asteroids:
        while stack and asteroid and stack[-1] > 0 and asteroid < 0:
            diff = stack[-1] + asteroid
            if diff < 0:
                stack.pop()
            elif diff > 0:
                asteroid = 0
            else:
                asteroid = 0
                stack.pop()
        if asteroid:
            stack.append(asteroid)
    return stack

print(asteroidCollision([-2,-2,1,-10,5,-8,6,-4,-3,11,-11]))
