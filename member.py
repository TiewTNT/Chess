import pygame
import grid

WHITE_CIRCLE_PATH = './white_circle.png'
BLACK_CIRCLE_PATH = './black_circle.png'
WHITE_CIRCLE_X_PATH = './white_circle_x.png'
BLACK_CIRCLE_X_PATH = './black_circle_x.png'

all_grid_names = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8']

if __name__ != '__main__':
    white_circle = pygame.image.load(WHITE_CIRCLE_PATH).convert_alpha()
    white_circle = pygame.transform.scale(white_circle, (80, 80))
    black_circle = pygame.image.load(BLACK_CIRCLE_PATH).convert_alpha()
    black_circle = pygame.transform.scale(black_circle, (80, 80))
    white_circle_x = pygame.image.load(WHITE_CIRCLE_X_PATH).convert_alpha()
    white_circle_x = pygame.transform.scale(white_circle_x, (80, 80))
    black_circle_x = pygame.image.load(BLACK_CIRCLE_X_PATH).convert_alpha()
    black_circle_x = pygame.transform.scale(black_circle_x, (80, 80))

class Member:
    def __init__(self, is_white, screen, grid, is_dragging=False,  x=False):
        self.is_white =	is_white
        self.screen = screen
        self.grid = grid
        self.pos = (self.grid.start_point.x + 10, self.grid.start_point.y + 10)
        self.x = x
        self.is_dragging = is_dragging
        if self.is_white:
            if not self.x:
                self.appearance = 'white'
            else:
                self.appearance = 'white x'
        else:
            if not self.x:
                self.appearance = 'black'
            else:
                self.appearance = 'black x'

    def draw(self, pos):
        if self.is_dragging:
            self.pos = (pos[0] - 40, pos[1] - 40)

        if not self.x:
            if self.is_white:
                circle = white_circle
            elif self.is_white == False:
                circle = black_circle				
        else:
            if self.is_white:
                circle = white_circle_x
            elif self.is_white == False:
                circle = black_circle_x
        self.screen.blit(circle, self.pos)		

    def snap_grid(self):		
        self.pos = (self.grid.start_point.x + 10, self.grid.start_point.y + 10)

    def get_valid(self):
        ans = []
        char, num = self.grid.name
        match self.appearance:
            case 'white':
                valid = [(chr(ord(char) - 1)) + str(int(num) + 1), (chr(ord(char) + 1)) + str(int(num) + 1)]
            case 'black':
                valid = [(chr(ord(char) - 1)) + str(int(num) - 1), (chr(ord(char) + 1)) + str(int(num) - 1)]
            case 'white x':
                valid = []
                for i in range(7):
                    valid.append((chr(ord(char) - (i + 1))) + str(int(num) + (i + 1)))
                    valid.append((chr(ord(char) - (i + 1))) + str(int(num) - (i + 1)))
                    valid.append((chr(ord(char) + (i + 1))) + str(int(num) + (i + 1)))
                    valid.append((chr(ord(char) + (i + 1))) + str(int(num) - (i + 1)))

            case 'black x':
                valid = []
                for i in range(7):
                    valid.append((chr(ord(char) - (i + 1))) + str(int(num) + (i + 1)))
                    valid.append((chr(ord(char) - (i + 1))) + str(int(num) - (i + 1)))
                    valid.append((chr(ord(char) + (i + 1))) + str(int(num) + (i + 1)))
                    valid.append((chr(ord(char) + (i + 1))) + str(int(num) - (i + 1)))
        not_a_grid = []
        for grid_name in valid:
            if grid_name not in all_grid_names:
                not_a_grid.append(grid_name)
        for fake_grid in not_a_grid:
            valid.remove(fake_grid)
        return valid

def test1():
    print('running test1')
    circle = Member(True, None, grid.GridManager(None).get_grid('B2'), x=True)
    print(circle.get_valid())
    assert sorted(circle.get_valid()) == sorted(['A1', 'A3', 'C1', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8'])

def test2():
    print('running test2')
    circle = Member(True, None, grid.GridManager(None).get_grid('H1'), x=True)
    print(circle.get_valid())
    assert sorted(circle.get_valid()) == sorted(['A8', 'B7', 'C6', 'D5', 'E4', 'F3', 'G2'])


if __name__ == '__main__':	
    test1()	
    test2()		


    
        
        