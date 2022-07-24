import pygame

BLACK = (100, 100, 100)
WHITE = (200, 200, 200)

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

class Grid:
    def __init__(self, start_point, width, height, name, screen, color):
        assert type(start_point) == Point
        self.start_point = start_point
        self.color = color
        self.end_point = Point(start_point.x + width, start_point.y + height)
        self.width = width
        self.height = height
        self.center = Point(start_point.x + width / 2, start_point.y + height / 2)
        self.is_empty = True 
        self.name = name
        self.screen = screen
        self.rect = pygame.Rect(start_point.x, start_point.y, self.width, self.height)
        ...
        pass
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

        

class GridManager:
    def __init__(self, screen):
        self.screen = screen
        grid_list = []
        width, height = 100, 100
        for x, char1 in enumerate('ABCDEFGH'):
            for y, char2 in enumerate('12345678'):
                start_point = Point(0 + (x * width), (0 + y * height))
                name = char1 + char2
                if (x + y) % 2 == 0:
                    color = BLACK 
                else:
                    color = WHITE
                grid = Grid(start_point, width, height, name, self.screen, color)
                grid_list.append(grid)
        self.all_grids = grid_list

    def get_grid(self, name):
        for grid in self.all_grids:
            if grid.name == name:
                return grid
        assert False

    def draw_table(self):
        for grid in self.all_grids:
            grid.draw()

        
        
                

