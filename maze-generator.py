# Implements depth-first search with backtracking to generate the maze.
import pyglet as pyg
import random
from PQueue import PQueue
from Point import Point
import math

# Initial definitions and global variables
line_width = 1
rows = 5 
columns = 5
lines_list = [] 
squares = []
grid = None
current_point = None
current_square = None
explored_points = []
maze_completed = False
end_reached = False
optimal_path = []
maze = None

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
    grid = [[Point(x,y,columns,rows) for y in range(columns)] for x in range(rows)]
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
    global maze_completed
    global pyg
    global maze
    global current_square
    # if maze_completed:
    #     return
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
        print('Hey')

def h(point):
    "Calculates heuristic value for a given point to the end of grid."
    global end_point
    # Manhattan distance.
    # return abs(end_point.x - point.x) + abs(end_point.y - point.y)
    # Euclidean Distance.
    return math.sqrt((end_point.x - point.x)**2 + (end_point.y - point.y)**2)

frontier = PQueue()
visited_nodes = []
def draw2(delta_time):
    global lines_list
    global current_point
    global frontier
    global visited_nodes
    global end_point
    global end_reached
    if len(frontier.heap) > 0 and not end_reached:
        # print(f'frontier is: {frontier.heap}')
        cp = frontier.pop()
        # print(f'frontier is: {frontier.heap}')
        visited_nodes.append(cp)
        if cp.x == end_point.x and cp.y == end_point.y:
            end_reached = True
        
        # print(f'Current point walls: {cp.north_wall}, {cp.east_wall}, {cp.south_wall}, {cp.west_wall}')
        # print(f'Current point: {cp.x}, {cp.y}')
        for position in cp.neighbours:
            neighbour_x, neighbour_y, orientation = position
            # print(f'Neighbour x: {neighbour_x} | Neighbour y: {neighbour_y}')
            if orientation == "north" and cp.south_wall:
                continue
            elif orientation == "east" and cp.east_wall:
                continue
            elif orientation == "south" and cp.north_wall:
                continue
            elif orientation == "west" and cp.west_wall:
                continue
            neighbour = grid[neighbour_x][neighbour_y]
            # print(f'Neighbour is: {neighbour.x}, {neighbour.y}')
            # print(f'frontier is: {frontier.heap}')
            if neighbour not in visited_nodes:
                tentativeg = cp.g + 1

                if neighbour in frontier.heap:
                    neighbour.g = max(neighbour.g, tentativeg)

                neighbour.f = neighbour.g + h(neighbour)

                if neighbour not in frontier.heap:
                    neighbour.parent = cp
                    frontier.push(neighbour)

        draw_optimal_path(cp)

def draw_optimal_path(point):
    global optimal_path
    global width_factor
    global height_factor
    global batch
    global screen_height
    global GREEN
    square = pyg.shapes.BorderedRectangle(point.x*width_factor, (-(point.y*height_factor)+screen_height)-height_factor, width_factor, height_factor, border=0, color=GREEN, batch=batch)
    square.opacity = 100
    optimal_path.append(square)

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
start_point = current_point
end_point = grid[-1][-1]
frontier.push(start_point)
maze = pyg.clock.schedule_interval(draw, 1/30)

search_started = False

@screen.event
def on_draw():
    screen.clear()
    batch.draw()
    global maze_completed
    global maze
    global search_started
    global pyg
    if maze_completed and not search_started:
        search_started = True
        pyg.clock.unschedule(maze)
        pyg.clock.schedule_interval(draw2, 1/30)
pyg.app.run()
