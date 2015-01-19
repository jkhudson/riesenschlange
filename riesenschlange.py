import pygame
from pygame.locals import *
import sys
from random import randint
pygame.init()

size = width, height = 801, 601
black = 0,0,0
cyan = 0,255,255
line_spacing = 20
fps = 60
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Riesenschlange')
logo = pygame.image.load("logo.png").convert_alpha()
#pygame.display.set_icon(logo)
logorect = logo.get_rect()

class Hebi:
	def __init__(self):
		self.x, self.y = 0,0
	def get_x(self):
		return self.x
	def get_y(self):
		return self.y
	def set_x(self,x):
		self.x = x
	def set_y(self,y):
		self.y = y
	def move_x(self,x):
		self.x += x
		if self.x < 0:
			self.x = 0
		elif self.x > (width - line_spacing -1):
			self.x = (width - line_spacing -1)
	def move_y(self,y):
		self.y += y
		if self.y < 0:
			self.y = 0
		elif self.y > (height - line_spacing -1):
			self.y = (height - line_spacing -1)
class Ringo:
	def __init__(self):
		self.x = randint(0,(width-1)/line_spacing)
		self.y = randint(0,(height-1)/line_spacing)
	
	def get_x(self):
		return self.x

	def get_y(self):
		return self.y
hebi_list = []
ringo_list = []
myhebi = Hebi()
clock = pygame.time.Clock()
color_counter = 255 
darkening = True
while True:
	clock.tick(fps)
	if (len(ringo_list) < 5) and not(randint(0,999)%233): 
		ringo_list.append(Ringo())
	# line_spacing = randint(2,500)
	# color = (randint(1,255),randint(1,255),randint(1,255))
	color = black
	keys = pygame.key.get_pressed()
	if keys[K_w]: myhebi.move_y(-line_spacing)
	if keys[K_s]: myhebi.move_y(line_spacing)
	if keys[K_a]: myhebi.move_x(-line_spacing)
	if keys[K_d]: myhebi.move_x(line_spacing)
	if line_spacing <= 0: line_spacing = 1
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE: sys.exit()
			#elif event.key == K_w: line_spacing += 5
			#elif event.key == K_s: line_spacing -= 5	
	screen.fill(color)
	cyan = (0,color_counter,color_counter)
	if darkening:
		color_counter -= 3
		if color_counter <= 20: darkening = False
	else:
		color_counter += 3
		if color_counter >= 255: darkening = True
	for x in range(0, width, line_spacing):
		pygame.draw.line(screen, cyan, (x,0),(x,height))
	for y in range(0, height, line_spacing): 
		pygame.draw.line(screen, cyan, (0,y),(width,y))
	for ringo in ringo_list:
		pygame.draw.rect(screen,(255,0,0),(ringo.get_x()*line_spacing,ringo.get_y()*line_spacing,line_spacing,line_spacing))
	pygame.draw.rect(screen,(0,255,255),(myhebi.get_x(),myhebi.get_y(),20,20))
	screen.blit(logo,(350,250))
	pygame.display.flip()
