import pygame as pg


# def grid(screen, height, width, size, color):
#     for x in range(0, width, size):
#         for y in range(0, height, size):
#             rect = pg.Rect(x, y, size, size)
#             pg.draw.rect(screen, color, rect, 1)


def grid(screen, cell_size, color=(0, 0, 0)):
    width = screen.get_width()
    height = screen.get_height()

    for x in range(0, width, cell_size):
        pg.draw.line(screen, color, (0, x), (width, x))

    for y in range(0, height, cell_size):
        pg.draw.line(screen, color, (y, 0), (y, height))


def square(screen, x, y, size, color, width=0):
    pg.draw.polygon(screen, color, [(y*size, x*size),
                                    ((y+1)*size, x*size),
                                    ((y+1)*size, (x+1)*size),
                                    (y*size, (x+1)*size)], width)
