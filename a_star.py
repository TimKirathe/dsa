import pygame as pg
import math
import random

rows = 100
columns = 100

pg.init()

window_size = (805, 805)
screen = pg.display.set_mode(window_size)
pg.display.set_caption("A *")
screen_width = 800
screen_height = 800
width_factor = screen_width // columns
height_factor = screen_height // rows
margin = 0

# Implements a priority queue with the min-heap datatype.
class PQueue:
    def __init__(self):
        self.heap = []

    def push(self, point):
        self.heap.append(point)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_point = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_point
        
    def _heapify_up(self, position):
        while position > 0:
            parent_position = (position - 1) // 2
            if self.heap[position].f < self.heap[parent_position].f:
                self.heap[position], self.heap[parent_position] = self.heap[parent_position], self.heap[position]
                position = parent_position
            else:
                break
        
    def _heapify_down(self, position):
        left_child = 2*position + 1
        right_child = 2*position + 2
        smallest_position = position
        if left_child < len(self.heap) and self.heap[left_child].f < self.heap[smallest_position].f:
            smallest_position = left_child

        if right_child < len(self.heap) and self.heap[right_child].f < self.heap[smallest_position].f:
            smallest_position = right_child

        if smallest_position != position:
            self.heap[position], self.heap[smallest_position] = self.heap[smallest_position], self.heap[position]
            self._heapify_down(smallest_position) 

    def print_queue(self):
        print(self.heap)

class Point:
    def __init__(self, x, y, grid_width, grid_height):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.north, self.east, self.south, self.west, self.northw, self.northe, self.southe, self.southw = None, None, None, None, None, None, None, None
        self.parent = None
        self.neighbours = []
        self.get_neighbours(grid_width, grid_height)
        self.wall = False

        randint = random.random()
        if randint < 0.35:
            self.wall = True

    def show(self, surface, color, width_factor, height_factor):
        pg.draw.rect(surface, color, (self.x*width_factor, self.y*height_factor, width_factor - 1, height_factor - 1))

    def get_neighbours(self, width, height):
        # Neighbour directions are in order: North, East, South, West
        offsetN = self.x - 1
        offsetE = self.y + 1
        offsetS = self.x + 1
        offsetW = self.y - 1

        if offsetN >= 0:
            self.north = (offsetN, self.y)
            self.neighbours.append(self.north)
        if offsetE < width:
            self.east = (self.x, offsetE)
            self.neighbours.append(self.east)
        if offsetS < height:
            self.south = (offsetS, self.y)
            self.neighbours.append(self.south)
        if offsetW >= 0:
            self.west = (self.x, offsetW) 
            self.neighbours.append(self.west)
        if offsetW >= 0 and offsetN >= 0:
            self.northw = (offsetN, offsetW)
            self.neighbours.append(self.northw)
        if offsetE < width and offsetN >= 0:
            self.northe = (offsetN, offsetE)
            self.neighbours.append(self.northe)
        if offsetE < width and offsetS < height:
            self.southe = (offsetS, offsetE)
            self.neighbours.append(self.southe)
        if offsetW >= 0 and offsetS < height:
            self.southw = (offsetS, offsetW)
            self.neighbours.append(self.southw)

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

frontier = PQueue()
visited_nodes = []
optimal_path = []

search_grid = [[Point(x,y,columns, rows) for y in range(columns)] for x in range(rows)]
start_point = search_grid[0][0]
end_point = search_grid[-1][-1]
start_point.wall = False
end_point.wall = False
frontier.push(start_point)

def show_grid(grid):
    "Displays the search grid"
    global screen
    global BLACK
    global WHITE

    screen.fill(BLACK)
    for c in range(len(grid)):
        for r in range(len(grid[c])):
            if not grid[c][r].wall:
                grid[c][r].show(screen, WHITE, width_factor, height_factor)


def show_searches():
    global frontier
    global visited_nodes
    for i in range(len(frontier.heap)):
        frontier.heap[i].show(screen, GREEN, width_factor, height_factor)

    for j in range(len(visited_nodes)):
        visited_nodes[j].show(screen, RED, width_factor, height_factor)

def h(point):
    "Calculates heuristic value for a given point to the end of grid."
    global end_point
    # Manhattan distance.
    # return abs(end_point.x - point.x) + abs(end_point.y - point.y)
    # Euclidean Distance.
    return math.sqrt((end_point.x - point.x)**2 + (end_point.y - point.y)**2)

show_grid(search_grid)
pg.display.flip()

path_printed = False
end_reached = False
furthest_printed = False
running = True

while running:
    
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False

    while len(frontier.heap) > 0 and not end_reached:
        current_point = frontier.pop()
        visited_nodes.append(current_point)
        if current_point.x == end_point.x and current_point.y == end_point.y:
            # Get optimal path from parent pointers of end point.
            optimal_path.append(current_point)
            while current_point.parent:
                optimal_path.append(current_point.parent)
                current_point = current_point.parent
            end_reached = True

        for position in current_point.neighbours:
            neighbour_x, neighbour_y = position
            neighbour = search_grid[neighbour_x][neighbour_y]
            if neighbour not in visited_nodes and not neighbour.wall:
                tentativeg = current_point.g + 1

                if neighbour in frontier.heap:
                    neighbour.g = tentativeg if tentativeg < neighbour.g else neighbour.g
                
                neighbour.f = neighbour.g + h(neighbour)

                if neighbour not in frontier.heap:
                    neighbour.parent = current_point
                    frontier.push(neighbour)
        show_searches()
        pg.display.flip()
    
    if end_reached:
        # Show optimal path.
        if not path_printed:
            show_grid(search_grid)
            for i in range(len(optimal_path)):
                optimal_path[i].show(screen, BLUE, width_factor, height_factor)
            pg.display.flip()
            path_printed = True
    elif not furthest_printed:
        # Show furthest path reached.
        show_grid(search_grid)
        for i in range(len(visited_nodes)):
            visited_nodes[i].show(screen, BLUE, width_factor, height_factor)
        pg.display.flip()
        furthest_printed = True
    
pg.quit()