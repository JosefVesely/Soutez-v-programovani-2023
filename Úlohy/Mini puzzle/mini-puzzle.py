# Josef Veselý

import pygame as pg
from PIL import Image
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()


def get_files():
    filepaths = filedialog.askopenfilenames(title="Vyberte 4 obrázky", filetypes=(("JPEG Image","*.jpg"), ("all files","*.*")))
    return filepaths

filepaths = get_files()


# Constants
TITLE = "Mini Puzzle"

IMG_SIZE = 400
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
FPS = 60

# Init variables
pg.init()
pg.display.set_caption(TITLE)

running = True
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pg.time.Clock()

# Load images
img1 = pg.transform.scale(pg.image.load(filepaths[0]).convert(), (IMG_SIZE, IMG_SIZE))
img2 = pg.transform.scale(pg.image.load(filepaths[1]).convert(), (IMG_SIZE, IMG_SIZE))
img3 = pg.transform.scale(pg.image.load(filepaths[2]).convert(), (IMG_SIZE, IMG_SIZE))
img4 = pg.transform.scale(pg.image.load(filepaths[3]).convert(), (IMG_SIZE, IMG_SIZE))

# Game loop
while running:
    clock.tick(FPS)
    screen.fill(pg.Color("black"))

    # Handle input
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Update

    # Render
    


    screen.blit(img1, (0, 0))
    screen.blit(img2, (IMG_SIZE, 0))
    screen.blit(img3, (0, IMG_SIZE))
    screen.blit(img4, (IMG_SIZE, IMG_SIZE))


    pg.display.update()

pg.quit()