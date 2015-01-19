import pygame
from pygame.locals import *
import sys
from random import randint
pygame.init()

size = width, height = 800, 600
black = 0,0,0
blue = 0,255,255
line_spacing = 20
fps = 60
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Riesenschlange')
logo = pygame.image.load("logo.png")
logo = logo.convert_alpha()
logorect = logo.get_rect()

clock = pygame.time.Clock()

while True:
	clock.tick(fps)
	# line_spacing = randint(2,500)
	# color = (randint(1,255),randint(1,255),randint(1,255))
	color = black
	keys = pygame.key.get_pressed()
	if keys[K_w]: line_spacing += 5
	if keys[K_s]: line_spacing -= 5
	if line_spacing <= 0: line_spacing = 1
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE: sys.exit()
			#elif event.key == K_w: line_spacing += 5
			#elif event.key == K_s: line_spacing -= 5	
	screen.fill(color)
	for x in range(0, width, line_spacing):
		pygame.draw.line(screen, blue, (x,0),(x,height))
	for y in range(0, height, line_spacing): 
		pygame.draw.line(screen, blue, (0,y),(width,y))

	screen.blit(logo,(350,250))
	pygame.display.flip()
