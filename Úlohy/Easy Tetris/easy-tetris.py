# Josef Veselý

import pygame as pg
import easygui

# Constants
TITLE = "Easy Tetris"
SQUARE_SIZE = 48
COLS, ROWS = 10, 20
WINDOW_WIDTH = COLS * SQUARE_SIZE
WINDOW_HEIGHT = ROWS * SQUARE_SIZE
FPS = 6

# Init variables
pg.init()
pg.display.set_caption(TITLE)

global running
global points
points = 0
running = True
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pg.time.Clock()



class Grid:
    def __init__(self):
        self.grid = [[0 for i in range(COLS)] for j in range(ROWS)]

        self.grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        
    def draw(self, screen):
        for i in range(1, COLS+1):
            pg.draw.line(screen, pg.Color("gray"), (i*SQUARE_SIZE, 0), (i*SQUARE_SIZE, ROWS*SQUARE_SIZE), width=1)

        for i in range(1, ROWS+1):
            pg.draw.line(screen, pg.Color("gray"), (0, i*SQUARE_SIZE), (ROWS*SQUARE_SIZE, i*SQUARE_SIZE), width=1)

    def update(self, grid, collided: bool):
        self.delete_layers(grid, collided)

    def delete_layers(self, grid, collided: bool):
        global points
        if not collided:
            return
        
        # Vymaž kostky
        for i, line in enumerate(grid.grid):
            #print(line)

            if line == [1] * COLS:
                grid.grid[i] = [0] * COLS
                points += 1

        # Posuň kostky
        # grid.grid = grid.grid[:-2]
        # grid.grid.insert(0, [0]*COLS)
        # print(f"{len(grid.grid)=} {len(grid.grid[0])=}")
        # print("test")


class Block:
    def __init__(self):
        self.x = 4
        self.y = 0
        self.collided = False


    def get_block_points(self):
        return [(self.x, self.y), (self.x+1, self.y), (self.x, self.y+1), (self.x+1, self.y+1)]
    
    def draw(self, screen, grid):
        for y in range(ROWS):
            for x in range(COLS):
                if grid.grid[y][x] == 1:
                    pg.draw.rect(screen, pg.Color("goldenrod1"), pg.Rect(x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        pg.draw.rect(screen, pg.Color("goldenrod1"), pg.Rect(self.x*SQUARE_SIZE, self.y*SQUARE_SIZE, 2*SQUARE_SIZE, 2*SQUARE_SIZE))


    def update(self):
        self.y += 1

    def check_collision(self, grid):
        global running
        for block_point in self.get_block_points():
            x, y = block_point
            try:
                if grid.grid[y+1][x] == 1:
                    #print("Collided")
                    self.update_grid(grid)

                    if y == 1:
                        running = False
                        #print("Game over 2")
            except IndexError: # narazil na hranu obrazovky
                self.update_grid(grid)

    def update_grid(self, grid):
        # update grid
        global points
        for block_point in self.get_block_points():
            x, y = block_point
            #print(self.get_block_points())
            grid.grid[y][x] = 1
        
        self.collided = True


grid = Grid()
block = Block()
points = 0

# Game loop
while True:
    while running:
        clock.tick(FPS)
        screen.fill((50, 50, 50))

        # Handle input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

            # Keyboard
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    if block.x > 0:
                        block.x -= 1
                if event.key == pg.K_RIGHT:
                    if block.x + 2 < COLS:
                        block.x += 1
                # if event.key == pg.K_DOWN:
                #     block.fall_down(grid)
                    


        # Update
        block.update()
        block.check_collision(grid)
        grid.update(grid, block.collided)

        if block.collided:
            del block
            block = Block()

        # Render
        block.draw(screen, grid)
        grid.draw(screen)

        pg.display.update()

    easygui.msgbox(f"Prohrál jsi! Skóre: {points}", "Prohrál jsi!", ok_button="Hrát znova")
    del grid, block
    block = Block()
    grid = Grid()
    points = 0
    running = True

pg.quit()