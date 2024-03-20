# Time complexity: O(n) | Space complexity: O(1) 
def findAltitude(gain):
    altitude = 0
    highest = 0
    for i in range(len(gain)):
        altitude += gain[i]
        highest = max(highest, altitude)
    return highest

print(findAltitude([-5,-3, -1, 3, 1, 1, -5, 7]))
