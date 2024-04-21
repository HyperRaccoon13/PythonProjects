import time
import pygame
import numpy as np


WIDTH, HEIGHT = 800, 600
SIZE = 10

backgroundColour = (10, 10, 10)
gridColour = (40, 40, 40)
cellDieNextColour = (170, 170, 170) #(255, 0, 0)#
cellAliveNextColour = (255, 255, 255) #(0, 255, 0)#


def Update(screen, cells, size, withProgress=False):
    UpdateCells = np.zeros((cells.shape[0], cells.shape[1]))
    
    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row - 1 : row + 2, col - 1 : col + 2]) - cells[row, col]
        colour = backgroundColour if cells[row, col] == 0 else cellAliveNextColour

        if cells[row, col] == 1:
            if alive < 2  or alive > 3:
                if withProgress: 
                    colour = cellDieNextColour

            elif 2 <= alive <= 3:
                UpdateCells[row, col] = 1
                if withProgress:
                    colour = cellAliveNextColour

        else: 
            if alive == 3:
                UpdateCells[row, col] = 1
                if withProgress:
                    colour = cellAliveNextColour
        
        pygame.draw.rect(screen, colour, (col * size, row * size, size - 1, size - 1))

    return UpdateCells

def main():

    pygame.init()
    pygame.display.set_caption("Game Of Life")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
   

    cells = np.zeros((60, 80))
    screen.fill(gridColour)
    Update(screen, cells, SIZE)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    Update(screen, cells, SIZE)
                    pygame.display.update()

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // SIZE, pos[0] // SIZE] = 1
                Update(screen, cells, SIZE)
                pygame.display.update()

        screen.fill(gridColour)


        if running:
            cells = Update(screen, cells, SIZE, withProgress=True)
            pygame.display.update()

        time.sleep(0.001)

if __name__ == "__main__":
    main()