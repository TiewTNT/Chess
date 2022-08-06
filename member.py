import pygame

WHITE_CIRCLE_PATH = './white_circle.png'
BLACK_CIRCLE_PATH = './black_circle.png'
WHITE_CIRCLE_X_PATH = './white_circle_x.png'
BLACK_CIRCLE_X_PATH = './black_circle_x.png'


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

	def draw(self, pos):
		if self.is_dragging:
			self.pos = pos

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

	def drag(self):
		...																																																																																																
