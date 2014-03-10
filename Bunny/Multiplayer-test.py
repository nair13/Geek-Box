# Multiplayer in Bunnies 25/10/13

#1 import the libraries

import pygame
from pygame.locals import *
import math
import random

#2 initialize the game

pygame.init()
width = 640
height = 480
screen = pygame.display.set_mode((width,height))

keys1 = [False,False]
keys2 = [False,False]

arrows = []

#3 Load images

player1 = pygame.image.load("resources/images/dude.png")
player2 = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
arrow = pygame.image.load("resources/images/bullet.png")
pos1 = [100,100]

#4 Keep looping through
while True:
	#5 Clear screen before drawing it again
	screen.fill(0)
	
	#6 Draw Elements
	for x in range(width/grass.get_width()+1):
		for y in range(height/grass.get_height()+1):
			screen.blit(grass,(x*100,y*100))
	
	screen.blit(player1,pos1)
	#6.1 Draw arrows	
	screen.blit(arrow, (pos1[0],pos1[1]+25))
	#7 Update the screen
	pygame.display.flip()

	#8 Loop through events
	for event in pygame.event.get():
		#9 Check if the event is quit(x)
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
		#10 Keypress events
		if event.type == pygame.KEYDOWN:
			if event.key == K_w:
				keys1[0] = True
			elif event.key == K_s:
				keys1[1] = True
			if event.key == K_j:
				arrows.append()
		if event.type == pygame.KEYUP:
			if event.key == K_w:
				keys1[0] = False
			elif event.key == K_s:
				keys1[1] = False
		#10.1 Arrow
		
	#11 Movement
	if keys1[0]:
		pos1[1] -= 5
	elif keys1[1]:
		pos1[1] += 5 
