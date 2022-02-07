import numpy as np
import pygame
import time
from src import draw, constants as c
from core import logger


def main():

    # Logger
    log = logger.Logger('main')

    # Initialize screen
    pygame.init()
    screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    screen.fill(c.WHITE)

    # Initialize grid
    # Alive = 1 ; Dead = 0
    game_state = np.zeros((c.X_CELLS, c.Y_CELLS))

    game_state[2, 2] = 1
    game_state[2, 3] = 1
    game_state[2, 4] = 1

    running = True
    pause = True
    while running:

        new_game_state = np.copy(game_state)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pause = not pause

            mouse_click = pygame.mouse.get_pressed()
            if any(mouse_click):
                x_pos, y_pos = pygame.mouse.get_pos()
                x_cell, y_cell = int(
                    np.floor(x_pos/c.CELL_WIDTH)), int(np.floor(y_pos/c.CELL_HEIGHT))
                new_game_state[x_cell, y_cell] = not mouse_click[2]

        # time.sleep(0.01)

        for y in range(c.X_CELLS):
            for x in range(c.Y_CELLS):

                n_neighbours = game_state[(x-1) % c.X_CELLS, (y-1) % c.Y_CELLS] + \
                    game_state[x % c.X_CELLS, (y-1) % c.Y_CELLS] + \
                    game_state[(x+1) % c.X_CELLS, (y-1) % c.Y_CELLS] + \
                    game_state[(x-1) % c.X_CELLS, y % c.Y_CELLS] + \
                    game_state[(x+1) % c.X_CELLS, y % c.Y_CELLS] + \
                    game_state[(x-1) % c.X_CELLS, (y+1) % c.Y_CELLS] + \
                    game_state[x % c.X_CELLS, (y+1) % c.Y_CELLS] + \
                    game_state[(x+1) % c.X_CELLS, (y+1) % c.Y_CELLS]

                # Game rules
                if not pause:
                    # Rule 1: Any dead cell with three live neighbours becomes a live cell.
                    if not game_state[x, y] and n_neighbours == 3:
                        new_game_state[x, y] = 1

                    # Any live cell with a different number of two or three live neighbours dies.
                    elif game_state[x, y] and (n_neighbours < 2 or n_neighbours > 3):
                        new_game_state[x, y] = 0

                # Draw screen
                if new_game_state[x, y]:
                    draw.square(screen, y, x, c.CELL_HEIGHT, c.BLACK)
                else:
                    draw.square(screen, y, x, c.CELL_HEIGHT, c.WHITE)

                draw.grid(screen, c.HEIGHT, c.WIDTH, c.CELL_HEIGHT, c.BLACK)

        game_state = np.copy(new_game_state)

        pygame.display.flip()


if __name__ == '__main__':
    main()
