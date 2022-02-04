import pygame as pg


def grid(screen, height, width, size, color):
    for x in range(0, width, size):
        for y in range(0, height, size):
            rect = pg.Rect(x, y, size, size)
            pg.draw.rect(screen, color, rect, 1)


def square(screen, x, y, size, color):
    pg.draw.polygon(screen, color, [(y*size, x*size),
                                    ((y+1)*size, x*size),
                                    ((y+1)*size, (x+1)*size),
                                    (y*size, (x+1)*size)])
