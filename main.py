import pygame
import grid
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Chess')

grid_manager = grid.GridManager(screen)

# Run until the user asks to quit♦
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    # Fill the background with white
    screen.fill((255, 255, 255))
    grid_manager.draw_table()

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()