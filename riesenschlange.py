import pygame
from pygame.locals import *
import sys
from random import randint
pygame.init()

size = width, height = 800, 600
black = 0,0,0
fps = 60
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Riesenschlange')
logo = pygame.image.load("logo.png")
logo = logo.convert_alpha()
logorect = logo.get_rect()

clock = pygame.time.Clock()

while True:
	clock.tick(fps)
	color = (randint(1,255),randint(1,255),randint(1,255))
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE: sys.exit()
	screen.fill(color)
	screen.blit(logo,(350,250))
	pygame.display.flip()
