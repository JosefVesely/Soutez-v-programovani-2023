# Documentation: https://www.pygame.org/docs/
import pygame as pg

# Constants
TITLE = "Title"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Init variables
pg.init()
pg.mixer.init()
pg.display.set_caption(TITLE)

running = True
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pg.time.Clock()


# Game loop
while running:
    clock.tick(FPS)
    screen.fill(pg.Color("black"))

    # Handle input
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # Keyboard
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                pass

        # Mouse
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1: # Left click
                mouse_pos = pg.mouse.get_pos()

    # Update

    # Render

    pg.display.update()

pg.quit()