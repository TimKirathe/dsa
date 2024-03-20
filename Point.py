import random
# Class definitions
class Point:
    def __init__(self, x, y, grid_width, grid_height):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        # Boundaries represent the walls of the point in the grid. Order is: North, East, South, West.
        self.north_wall = True
        self.east_wall = True
        self.south_wall = True
        self.west_wall = True
        self.north, self.east, self.south, self.west, self.northw, self.northe, self.southe, self.southw = None, None, None, None, None, None, None, None
        self.parent = None
        self.neighbours = []
        self.get_neighbours(grid_width, grid_height)
        self.visited = False

    def get_neighbours(self, width, height):
            # Neighbour directions are in order: North, East, South, West
            offsetW = self.x - 1
            offsetN = self.y + 1
            offsetE = self.x + 1
            offsetS = self.y - 1

            if offsetN < height:
                self.north = (self.x, offsetN, "north")
                self.neighbours.append(self.north)
            if offsetE < width:
                self.east = (offsetE, self.y, "east")
                self.neighbours.append(self.east)
            if offsetS >= 0:
                self.south = (self.x, offsetS, "south")
                self.neighbours.append(self.south)
            if offsetW >= 0:
                self.west = (offsetW, self.y, "west") 
                self.neighbours.append(self.west)

    def get_random_neighbour(self, grid_width, grid_height, grid):
        neighbours = []
        if self.x > 0:
            west_neighbour = grid[self.x-1][self.y]
            if not west_neighbour.visited:
                neighbours.append(west_neighbour)
        if self.y < grid_height - 1:
            north_neighbour = grid[self.x][self.y+1]
            if not north_neighbour.visited:
                neighbours.append(north_neighbour)
        if self.x < grid_width - 1:
            east_neighbour = grid[self.x+1][self.y]
            if not east_neighbour.visited:
                neighbours.append(east_neighbour)
        if self.y > 0:
            south_neighbour = grid[self.x][self.y-1]
            if not south_neighbour.visited:
                neighbours.append(south_neighbour)
        
        if len(neighbours) > 0:
            return random.choice(neighbours)
        return None
