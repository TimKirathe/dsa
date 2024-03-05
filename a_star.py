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
frontier = []
visited_nodes = []

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

search_grid = [[Point(x,y) for y in range(columns)] for x in range(rows)]
start_point = search_grid[0][0]
end_point = search_grid[-1][-1]
frontier.append(start_point)


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