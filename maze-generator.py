# Implements depth-first search with backtracking to generate the maze.
import pyglet as pyg
import random

# Initial definitions and global variables
line_width = 1
rows = 60
columns = 60
lines_list = [] 
squares = []
grid = None
current_point = None
current_square = None
explored_points = []

screen_width = 700
screen_height = 700
screen = pyg.window.Window(screen_width+10, screen_height+10)
width_factor = screen_width // columns
height_factor = screen_height // rows

batch = pyg.graphics.Batch()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GOLD = (206, 196, 51)

# Class definitions
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Boundaries represent the walls of the point in the grid. Order is: North, East, South, West.
        self.north_wall = True
        self.east_wall = True
        self.south_wall = True
        self.west_wall = True
        self.visited = False

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

def draw_walls(point):
    global lines_list
    global width_factor
    global height_factor
    global batch
    global screen_height
    global line_width
    if point.north_wall:
        lines_list.append(pyg.shapes.Line(point.x*width_factor, -(point.y*height_factor) + screen_height, point.x*width_factor+width_factor, -point.y*height_factor + screen_height, line_width, WHITE, batch))
    
    if point.east_wall:
        lines_list.append(pyg.shapes.Line(point.x*width_factor+width_factor, -point.y*height_factor + screen_height, point.x*width_factor+width_factor, -(point.y*height_factor+height_factor)+screen_height, line_width, WHITE, batch))
    
    if point.south_wall:
        lines_list.append(pyg.shapes.Line(point.x*width_factor+width_factor, -(point.y*height_factor+height_factor) +screen_height, point.x*width_factor, -(point.y*height_factor+height_factor) + screen_height, line_width, WHITE, batch))
    
    if point.west_wall:
        lines_list.append(pyg.shapes.Line(point.x*width_factor, -(point.y*height_factor+height_factor)+screen_height, point.x*width_factor, -(point.y*height_factor) + screen_height, line_width, WHITE, batch))


def draw_cell(point):
    global squares
    global width_factor
    global height_factor
    global batch
    global screen_height
    square = pyg.shapes.BorderedRectangle(point.x*width_factor, (-(point.y*height_factor)+screen_height)-height_factor, width_factor, height_factor, border=0, color=(91, 99, 183), batch=batch)
    square.opacity = 100
    squares.append(square)

def draw_current_point(cp):
    global batch
    global current_square
    current_square = pyg.shapes.BorderedRectangle(cp.x*width_factor, (-(cp.y*height_factor)+screen_height)-height_factor, width_factor, height_factor, border=0, color=GREEN, batch=batch)
    current_square.opacity = 100

def setup():
    global current_point
    global grid
    global width_factor
    global height_factor
    global batch
    global explored_points
    grid = [[Point(x,y) for y in range(columns)] for x in range(rows)]
    grid[0][0].visited = True
    current_point = grid[0][0]    
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            draw_walls(grid[c][r])
    current_point.visited = True
    draw_cell(current_point)
    
    
def draw(delta_time):
    global current_point
    global rows
    global columns
    global explored_points
    global grid
    draw_current_point(current_point)
    next_neighbour = current_point.get_random_neighbour(columns, rows, grid) 
    if next_neighbour:
        next_neighbour.visited = True
        remove_walls(current_point, next_neighbour)
        explored_points.append(current_point)
        current_point = next_neighbour
        draw_cell(next_neighbour)
    elif len(explored_points) > 0:
        current_point = explored_points.pop()

    
def remove_walls(current_point, next_neighbour):
    global lines_list
    if current_point.y - 1 == next_neighbour.y:
        # Remove north wall of current point and south wall of it's north neighbour.
        current_point.north_wall, next_neighbour.south_wall = False, False
        cp_nw_index = get_index(current_point.y, current_point.x, 0)
        lines_list[cp_nw_index] = None
        nn_sw_index = get_index(next_neighbour.y, next_neighbour.x, 2)
        lines_list[nn_sw_index] = None
    elif current_point.x + 1 == next_neighbour.x:
        # Remove east wall of current point and west wall of it's east neighbour.
        current_point.east_wall, next_neighbour.west_wall = False, False
        cp_ew_index = get_index(current_point.y, current_point.x, 1)
        lines_list[cp_ew_index] = None
        nn_ww_index = get_index(next_neighbour.y, next_neighbour.x, 3)
        lines_list[nn_ww_index] = None
    elif current_point.y + 1 == next_neighbour.y:
        # Remove south wall of current point and north wall of it's south neighbour.
        current_point.south_wall, next_neighbour.north_wall = False, False
        cp_sw_index = get_index(current_point.y, current_point.x, 2)
        lines_list[cp_sw_index] = None
        nn_nw_index = get_index(next_neighbour.y, next_neighbour.x, 0)
        lines_list[nn_nw_index] = None
    elif current_point.x - 1 == next_neighbour.x:
        # Remove west wall of current point and east wall of it's west neighbour.
        current_point.west_wall, next_neighbour.east_wall = False, False
        cp_ww_index = get_index(current_point.y, current_point.x, 3)
        lines_list[cp_ww_index] = None
        nn_ew_index = get_index(next_neighbour.y, next_neighbour.x, 1)
        lines_list[nn_ew_index] = None

def get_index(i, k, l):
    global columns
    return (4 * columns * i) + (4*k) + l

setup()
pyg.clock.schedule_interval(draw, 1/30)
@screen.event
def on_draw():
    screen.clear()
    batch.draw()

pyg.app.run()
