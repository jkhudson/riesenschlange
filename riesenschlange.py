import pygame
from pygame.locals import *
import sys
from random import randint
pygame.init()

size = width, height = 801, 601
black = 0,0,0
cyan = 0,255,255
line_spacing = 20
fps = 20
screen = pygame.display.set_mode((900,700))
pygame.display.set_caption('Riesenschlange')
logo = pygame.image.load("logo.png").convert_alpha()
#pygame.display.set_icon(logo)
logorect = logo.get_rect()

class Hebi:
	def __init__(self):
		self.x, self.y = 0,0
		self.old_x, self.old_y = 0,0
		self.length = 1
		self.left = 0
		self.right = 1
		self.up = 2
		self.down = 3
		self.direction = self.right
		self.old_direction = self.right
		self.color = (randint(127, 255),randint(127,255),randint(127,255))
		self.segment = None
		
	def get_color(self):
		return self.color
	def set_color(self, color):
		self.color = color
	def get_length(self):
		return self.length
	def set_direction(self, direction):
		self.direction = direction
	def grow(self):
		self.length += 1
		if self.segment:
			self.segment.grow()
			return
		self.segment = Hebi()
		hebi_list.append(self.segment)
		self.segment.set_color(self.color)
		self.segment.set_x(self.old_x)
		self.segment.set_y(self.old_y)
		self.segment.set_direction(self.direction)
		self.update()
		
	def get_x(self):
		return self.x
	def get_y(self):
		return self.y
	def set_x(self,x):
		self.x = x
	def set_y(self,y):
		self.y = y
	def move_x(self,x):
		self.old_x = self.x
		self.x += x
		if self.x < 0:
			self.x = 0
		elif self.x >= (width-1)/line_spacing-1:
			self.x = (width-1)/line_spacing-1
	def move_y(self,y):
		self.old_y = self.y
		self.y += y
		if self.y < 0:
			self.y = 0
		elif self.y >= (height-1)/line_spacing-1:
			self.y = (height-1)/line_spacing-1
	def move_left(self):
		self.move_x(-1)
		self.old_direction = self.direction
		self.direction = self.left
	def move_right(self):
		self.move_x(1)
		self.old_direction = self.direction
		self.direction = self.right
	def move_up(self):
		self.move_y(-1)
		self.old_direction = self.direction
		self.direction = self.up
	def move_down(self):
		self.move_y(1)
		self.old_direction = self.direction
		self.direction = self.down
	def rand_dir(self):
		self.direction = randint(0,3)
	def update(self):
		if self.direction == self.left:
			self.move_left()
		elif self.direction == self.right:
			self.move_right()
		elif self.direction == self.up:
			self.move_up()
		elif self.direction == self.down:
			self.move_down()
		if self.segment: 
			self.segment.set_direction(self.old_direction)
			self.segment.set_x(self.old_x)
			self.segment.set_y(self.old_y)
			#self.segment.update()

class NewHebi:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.left = 0
		self.right = 1
		self.up = 2
		self.down = 3
		self.direction = self.right
		self.nexthebi = None
	def set_x(self,x):
		self.x = x
	def set_y(self,y):
		self.y = y
	def get_x(self):
		return self.x
	def get_y(self):
		return self.y
	def grow(self):
		self.nexthebi = NewHebi(self.x, self.y)
		hebi_list.append(self.nexthebi)
	def move_up(self):
		if self.nexthebi:
			self.nexthebi.set_y(self.y)
			self.nexthebi.set_x(self.x)
		self.y -= 1
		self.direction = self.up
	def move_down(self):
		if self.nexthebi:
			self.nexthebi.set_y(self.y)
			self.nexthebi.set_x(self.x)
		self.y += 1
		self.direction = self.down
	def move_left(self):
		if self.nexthebi:
			self.nexthebi.set_y(self.y)
			self.nexthebi.set_x(self.x)
		self.x -= 1
		self.direction = self.left
	def move_right(self):
		if self.nexthebi:
			self.nexthebi.set_y(self.y)
			self.nexthebi.set_x(self.x)
		self.x += 1
		self.direction = self.right
	def update(self):
		if self.direction == self.left:
			self.move_left()
		elif self.direction == self.right:
			self.move_right()
		elif self.direction == self.up:
			self.move_up()
		elif self.direction == self.down:
			self.move_down()

class Ringo:
	def __init__(self):
		self.x = randint(0,(width-1)/line_spacing-1)
		self.y = randint(0,(height-1)/line_spacing-1)
	
	def get_x(self):
		return self.x

	def get_y(self):
		return self.y
def draw_grid(screen, width, height, line_spacing, color):
	for x in range(0, width, line_spacing):
		pygame.draw.line(screen, color, (x,0),(x,height-1))
	for y in range(0, height, line_spacing): 
		pygame.draw.line(screen, color, (0,y),(width-1,y))

hebi_list = []
ringo_list = []
myhebi = NewHebi(0,0)

hebi_list.append(myhebi)
#create a bunch of hebi, just for fun
#for i in range(0,9):
#	hebi_list.append(Hebi())
show_logo = True
clock = pygame.time.Clock()
color_counter = 255 
darkening = True
while True:
	clock.tick(fps)
	if (len(ringo_list) < 10) and not(randint(0,999)%3): 
		ringo_list.append(Ringo())
	# line_spacing = randint(2,500)
	# color = (randint(1,255),randint(1,255),randint(1,255))
	keys = pygame.key.get_pressed()
	if keys[K_w]: myhebi.move_up()
	if keys[K_s]: myhebi.move_down()
	if keys[K_a]: myhebi.move_left()
	if keys[K_d]: myhebi.move_right()
	#if line_spacing <= 0: line_spacing = 1
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE: sys.exit()
			#elif event.key == K_w: line_spacing += 5
			#elif event.key == K_s: line_spacing -= 5	
	screen.fill(black)
	cyan = (0,color_counter,color_counter)
	if darkening:
		color_counter -= 3
		if color_counter <= 20: darkening = False
	else:
		color_counter += 3
		if color_counter >= 255: darkening = True

	draw_grid(screen, width, height, line_spacing, cyan)
	
	#myhebi.update()
	#myhebi.rand_dir()
		

	for ringo in ringo_list:
		pygame.draw.rect(screen,(255,0,0),(ringo.get_x()*line_spacing+1,ringo.get_y()*line_spacing+1,line_spacing-1,line_spacing-1))
		for hebi in hebi_list:
			if ringo.get_x() == hebi.get_x() and ringo.get_y() == hebi.get_y():
				ringo_list.remove(ringo)
				hebi.grow()
				break

	for hebi in hebi_list:
		hebi.update()
		#hebi.rand_dir()
		pygame.draw.rect(screen,cyan,(hebi.get_x()*line_spacing+1,hebi.get_y()*line_spacing+1,line_spacing-1,line_spacing-1))
	if len(ringo_list) >= 5: show_logo = False 
	if show_logo: screen.blit(logo,(350,250))
	pygame.display.flip()
