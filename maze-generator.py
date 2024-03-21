# Implements depth-first search with backtracking to generate the maze.
import pyglet as pyg
import random
from PQueue import PQueue
from Point import Point
import math
import sys


# Initial definitions and global variables
line_width = 1
rows = int(sys.argv[1]) 
columns = int(sys.argv[2])

if not rows and not columns:
    print('Invalid parameters. You must give both a row number and column number.')
    sys.exit()
elif rows != columns:
    print('Rows and Columns must be equal.')
    sys.exit()


lines_list = [] 
squares = []
grid = None
current_point = None
current_square = None
explored_points = []
maze_completed = False
end_reached = False
optimal_path = []
search_started = False

screen_width = 700
screen_height = 700
screen = pyg.window.Window(screen_width+10, screen_height+10)
width_factor = screen_width // columns
height_factor = screen_height // rows

batch = pyg.graphics.Batch()
clk = pyg.clock.get_default()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


# Draw functions
def draw_walls(point):
    "Draws the walls for each point in the grid."
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
    "Draws all visited cells during the maze generation."
    global squares
    global width_factor
    global height_factor
    global batch
    global screen_height
    square = pyg.shapes.BorderedRectangle(point.x*width_factor, (-(point.y*height_factor)+screen_height)-height_factor, width_factor, height_factor, border=0, color=(91, 99, 183), batch=batch)
    square.opacity = 100
    squares.append(square)

def draw_current_point(cp):
    "Draws the current point in the maze creation."
    global batch
    global current_square
    current_square = pyg.shapes.BorderedRectangle(cp.x*width_factor, (-(cp.y*height_factor)+screen_height)-height_factor, width_factor, height_factor, border=0, color=GREEN, batch=batch)
    current_square.opacity = 100

def draw_maze(delta_time):
    "Main code that draws and implements the maze creation"
    global current_point
    global rows
    global columns
    global explored_points
    global grid
    global maze_completed
    global current_square

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

    if len(explored_points) == 0:
        maze_completed = True
        current_square = None


def setup():
    "Initial setup function for maze generation"
    global current_point
    global grid
    global width_factor
    global height_factor
    global batch
    global explored_points
    grid = [[Point(x,y,columns,rows) for y in range(columns)] for x in range(rows)]
    grid[0][0].visited = True
    current_point = grid[0][0]    
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            draw_walls(grid[c][r])
    current_point.visited = True
    draw_cell(current_point)


def remove_walls(current_point, next_neighbour):
    "Removes the walls of the current point and its next neighbour for the maze creation to continue"
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
    "Gets the index of a particular wall (north, east, south, west) in lines_list which is a flattened list based on the ordering of the grid"
    global columns
    return (4 * columns * i) + (4*k) + l

setup()
clk.schedule_interval(draw_maze, 1/30)

# A* search code

frontier = PQueue()
visited_nodes = []
start_point = current_point
end_point = grid[-1][-1]
frontier.push(start_point)


def h(point):
    "Calculates heuristic value for a given point to the end of grid."
    global end_point
    # Manhattan distance.
    # return abs(end_point.x - point.x) + abs(end_point.y - point.y)
    # Euclidean Distance.
    return math.sqrt((end_point.x - point.x)**2 + (end_point.y - point.y)**2)


def draw_search(delta_time):
    "Main code for displaying the A* search process."
    global lines_list
    global current_point
    global frontier
    global visited_nodes
    global end_point
    global end_reached
    global optimal_path
    if len(frontier.heap) > 0 and not end_reached:
        cp = frontier.pop()
        visited_nodes.append(cp)
        if cp.x == end_point.x and cp.y == end_point.y:
            end_reached = True
        
        for position in cp.neighbours:
            neighbour_x, neighbour_y, orientation = position
            if orientation == "north" and cp.south_wall:
                continue
            elif orientation == "east" and cp.east_wall:
                continue
            elif orientation == "south" and cp.north_wall:
                continue
            elif orientation == "west" and cp.west_wall:
                continue
            neighbour = grid[neighbour_x][neighbour_y]

            if neighbour not in visited_nodes:
                tentativeg = cp.g + 1

                if neighbour in frontier.heap:
                    neighbour.g = max(neighbour.g, tentativeg)

                neighbour.f = neighbour.g + h(neighbour)

                if neighbour not in frontier.heap:
                    neighbour.parent = cp
                    frontier.push(neighbour)

        optimal_path = []
        pseudo_optimal_path = []
        pseudo_optimal_path.append(cp)
        while cp.parent:
            pseudo_optimal_path.append(cp.parent)
            cp = cp.parent
        for p in pseudo_optimal_path:
            print(f'{p.x}, {p.y}')
            draw_optimal_path(p)

def draw_optimal_path(point):
    "Draws the optimal path of the A* search so far"
    global optimal_path
    global width_factor
    global height_factor
    global batch
    global screen_height
    global WHITE
    square = pyg.shapes.BorderedRectangle(point.x*width_factor, (-(point.y*height_factor)+screen_height)-height_factor, width_factor, height_factor, border=0, color=WHITE, batch=batch)
    square.opacity = 100
    optimal_path.append(square)


# Event listener for the in-built on_draw function offered by pyglet.
@screen.event
def on_draw():
    screen.clear()
    batch.draw()
    global maze_completed
    global search_started
    global clk
    if maze_completed and not search_started:
        search_started = True
        clk.unschedule(draw_maze)
        clk.schedule_interval(draw_search, 1/3000)

# Runs the pyglet app.
pyg.app.run()


# To run properly make sure to have pyglet installed.
# If you don't have pyglet run this on terminal: pip install pyglet
# Example run:
#  python3 maze-generator.py 50 50
#  * Will generate a 50 x 50 maze, the numbers must be the same
# Note: You must also pull PQueue.py & Point.py from same repo
