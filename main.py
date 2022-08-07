import pygame
import grid

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Chess')

import member

g = None

grid_manager = grid.GridManager(screen)

whites = []
blacks = []

for char in ['A2', 'B1', 'C2', 'D1', 'E2', 'F1', 'G2', 'H1']:
    whites.append(member.Member(True, screen, grid_manager.get_grid(char)))
for char in ['A8', 'B7', 'C8', 'D7', 'E8', 'F7', 'G8', 'H7']:
    blacks.append(member.Member(False, screen, grid_manager.get_grid(char)))

all_circles = whites + blacks
pressed = False

# Run until the user asks to quit
running = True
while running:

    mouse_pos = pygame.mouse.get_pos()
    mouse_presses = pygame.mouse.get_pressed()

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print('MOUSEBUTTONDOWN')
            print(mouse_pos)
            circle_to_del = []
            g = grid_manager.get_grid_by_pos(mouse_pos)
            for i, circle in enumerate(all_circles):
                if circle.grid == g:
                    circle.is_dragging = True
            


            
            
        if event.type == pygame.MOUSEBUTTONUP:
            print('MOUSEBUTTONUP')
            for circle in all_circles:
                if circle.is_dragging == True:
                    if circle.is_white == True:
                        char, num = circle.grid.name
                        if int(num) > 1:
                            valid = ((chr(ord(char) - 1)) + str(int(num) + 1), (chr(ord(char) + 1)) + str(int(num) + 1))
                            print(f'Valid: {valid[0]} or {valid[1]}')
                        else: 
                            print('End of board.')
                                





                    circle.is_dragging = False
                    g = grid_manager.get_grid_by_pos(mouse_pos)
                    print(g.name)
                    circle.grid = g
                    circle.snap_grid()
                    

    grid_manager.draw_table()
    for circle in all_circles:
        circle.draw(mouse_pos)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()