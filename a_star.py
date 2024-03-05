import pygame as pg

rows = 10
columns = 10

pg.init()

window_size = (830, 830)
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
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest_position]:
            smallest_position = left_child

        if right_child < len(self.heap) and self.heap[right_child] < self.heap[right_child].f < self.heap[smallest_position].f:
            smallest_position = right_child

        if smallest_position != position:
            self.heap[position], self.heap[smallest_position] = self.heap[smallest_position], self.heap[position]
            self._heapify_down(smallest_position) 

    def print_queue(self):
        print(self.heap)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0

    def show(self, surface, color, width_factor, height_factor):
        pg.draw.rect(surface, color, (self.x*width_factor, self.y*height_factor, width_factor - 1, height_factor - 1))

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

frontier = PQueue()
visited_nodes = []

search_grid = [[Point(x,y) for y in range(columns)] for x in range(rows)]
start_point = search_grid[0][0]
end_point = search_grid[-1][-1]
frontier.push(start_point)

def show_grid(grid):
    "Displays the search grid"
    global screen
    global RED
    global BLACK
    global GREEN
    global WHITE
    
    screen.fill(BLACK)
    for c in range(len(grid)):
        for r in range(len(grid[c])):
            grid[c][r].show(screen, WHITE, width_factor, height_factor)

    for i in range(len(frontier)):
        frontier[i].show(screen, GREEN, width_factor, height_factor)

    for j in range(len(visited_nodes)):
        visited_nodes[j].show(screen, RED, width_factor, height_factor)


running = True
while running:

    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False

    screen.fill(BLACK)

    show_grid(search_grid)
    pg.display.flip()

pg.quit()