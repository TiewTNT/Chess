import pygame

WHITE_CIRCLE_PATH = './white_circle.png'
BLACK_CIRCLE_PATH = './black_circle.png'
white_circle = pygame.image.load(WHITE_CIRCLE_PATH)
black_circle = pygame.image.load(BLACK_CIRCLE_PATH)

class Member:
	def __init__(self, is_white):
		self.is_white =	is_white
	def draw(self, grid):
		
