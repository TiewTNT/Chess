import pygame
from random import randint as r

pygame.init()

# screen setup 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chess')
###############################################################

# run flag
run = True
##########

# colors
BLACK = (90, 90, 90)
WHITE = (220, 220, 220)
#######################

GAP = 0

# square class
class Square:
    def __init__(s, screen, num_sq, pos, size, color_list=None, gap=0):
        assert type(pos) == tuple and len(pos) == 2
        if color_list != None:
            assert len(color_list) == num_sq
        assert type(gap) == int or gap == None
        assert type(size) == tuple

        s.screen = screen
        s.num = num_sq
        s.x, s.y = pos
        if color_list == None:
            s.color_list = []
            for i in range(num_sq):
                s.color_list.append((255, 50, 50))
        else:
            s.color_list = color_list
        s.width, s.height = size
        s.gap = gap
        s.w_total = s.width * s.num + s.gap * (s.num - 1)
        assert s.w_total <= s.screen.get_size()[0]
    def draw(s):
        for i in range(s.num):
            pygame.draw.rect(s.screen, s.color_list[i], pygame.Rect(s.x + i * s.gap, s.y, s.width, s.height))

    def center_draw(s):
        sc_width, sc_height = screen.get_size()
        start_x = sc_width / 2 - s.w_total / 2
        
        for i in range(s.num):
            pygame.draw.rect(s.screen, s.color_list[i], pygame.Rect(start_x + i * (s.gap + s.width), s.y, s.width, s.height))
            
##################################################################

# squares = Square(screen, 5, (0, 0), (60, 60), color_list=[(0, 0, 0), (210, 210, 210), (0, 0, 0), (210, 210, 210), (0, 0, 0)], gap=60)
# red_squares = Square(screen, 4, (15, 15), (30, 30), gap=61)

# main loop
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																										
            run = False

    screen.fill(BLACK)

    for i in range(8):
        if i % 2 == 1:
            Square(screen, 8, (0, 100 * i), (100, 100), color_list=[BLACK, WHITE, BLACK, WHITE, BLACK, WHITE, BLACK, WHITE], gap=GAP).center_draw()
        else:
            Square(screen, 8, (0, 100 * i), (100, 100), color_list=[WHITE, BLACK, WHITE, BLACK, WHITE, BLACK, WHITE, BLACK], gap=GAP).center_draw()
    pygame.draw.circle(screen, (r(1, 255), r(1, 255), r(1, 255)), [50, 750], 40, 0)
    pygame.display.update()
    
############################################################################################################################

############################
### quit pygame after loop #
############################
pygame.quit() ##############
############################