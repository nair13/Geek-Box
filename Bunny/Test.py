# First game  Bunnies vs Badgers 21-10-13

#1 import the library

import random
import math
import pygame 				# pygame is a python library used for game development
from pygame.locals import *


#2 initialize the game

pygame.init()
pygame.mixer.init()
width = 640
height = 480
screen = pygame.display.set_mode((width, height))

keys = [False,False,False,False]
playerpos = [100,100]

acc = [0,0]
arrows = []

badtimer = 200
badtimer1 = 0
badguys = [[640,1
00]]
healthvalue = 194
healthvalue2 = 194

#3 Load images

player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")
badguying1 = pygame.image.load("resources/images/badguy.png")
badguying = badguying1
healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
gameover = pygame.image.load("resources/images/gameover.png")
youwin = pygame.image.load("resources/images/youwin.png")


#3.1 Load Sound Effects

hit = pygame.mixer.Sound("resources/audio/explode.wav")
enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
pygame.mixer.music.load("resources/audio/moonlight.wav")
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.25)

#4 keep looping through

running = 1
exitcode = 0
while running:
	badtimer -= 1
	#5 clear the screen before drawing it again
	screen.fill(0)
	
	#6 draw screen elements
	for x in range(width/grass.get_width()+1):
		for y in range(height/grass.get_width()+1):
			screen.blit(grass,(x*100,y*100))
	screen.blit(castle,(0,30))
	screen.blit(castle,(0,135))
	screen.blit(castle,(0,240))
	screen.blit(castle,(0,345))
	#6.1 mouse rotation - (Okay this is why i should have payed attention in maths class!)
	position = pygame.mouse.get_pos()
	angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
	playerrot = pygame.transform.rotate(player, 360-angle*57.29)  # completely copied from sources
	playerpos1 = (playerpos[0]-playerrot.get_rect().width/2,playerpos[1]-playerrot.get_rect().height/2)	
	screen.blit(playerrot,playerpos1)

	#6.2 Draw arrow
	for bullet in arrows:
		index = 0
		velx = math.cos(bullet[0])*10
		vely = math.sin(bullet[0])*10
		bullet[1]+=velx
		bullet[2]+=vely
		if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 480:
			arrows.pop(index)
		index += 1
		for projectile in arrows:
			arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
			screen.blit(arrow1, (projectile[1], projectile[2]))

	#6.3 Draw badguys
	if badtimer==0:
        	badguys.append([0,random.randint(50,430)])
        	badtimer=200-(badtimer1*2)
        
		if badtimer1>=35:
            		badtimer1=35
        	else:
            		badtimer1+=5
    	index=0
    	index1 =0
	for badguy in badguys:
        	if badguy[0] > 640:
            		badguys.pop(index)
        	badguy[0]+=1
		#6.3.1 Attack castle -- attack bunny
		badrect = pygame.Rect(badguying.get_rect())
		playrect = pygame.Rect(player.get_rect())
		playrect.top = playerpos[1]
		playrect.left = playerpos[0]
		badrect.top = badguy[1]
		badrect.left = badguy[0]
			
		if badrect.colliderect(playrect):
			hit.play()
			healthvalue -= random.randint(5,20)
			badguys.pop(index)
		
		#6.3.2 Check for collision
		
		for bullet in arrows:
			bullrect = pygame.Rect(arrow.get_rect())
			bullrect.left = bullet[1]
			bullrect.top = bullet[2]
			if badrect.colliderect(bullrect):
				enemy.play()
				acc[0]+=1
				badguys.pop(index)
				arrows.pop(index1)
			if bullrect.left < 64:
				hit.play()
				healthvalue2 -= random.randint(5,20)
				arrows.pop(index1)		
        	index+=1
    	for badguy in badguys:
        	screen.blit(badguying, badguy)	
	#6.4 Add clock
	font = pygame.font.Font(None,24)
	survivedtext = font.render(str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2), True,(0,0,0))
	textRect = survivedtext.get_rect()
	textRect.topright = [320,5]
	screen.blit(survivedtext, textRect)	

	#6.5 Add Health bar -- second health bar
	screen.blit(healthbar, (5,5))
	
	for health1 in range(healthvalue):
		screen.blit(health, (health1+8,8))
	
	screen.blit(healthbar, (435,5))	
	for health2 in range(healthvalue2):
		screen.blit(health, (631-health2,8))	
	
	#7 update the sccreen
	pygame.display.flip()

	#8 loop through events
	for event in pygame.event.get():
		#9 check if the event is in the x button
		if event.type == pygame.QUIT:
			#10 if it is then quit
			pygame.quit()
			exit(0)
		#11 check if the event is key press		
		if event.type == pygame.KEYDOWN:  # setting the value to true in case of key down event
			if event.key == K_w:
				keys[0] = True
			elif event.key == K_a:
				keys[1] = True
			elif event.key == K_s:
				keys[2] = True
			elif event.key == K_d:
				keys[3] = True
		if event.type == pygame.KEYUP:
			if event.key == K_w:
				keys[0] = False
			elif event.key == K_a:
				keys[1] = False
			elif event.key == K_s:
				keys[2] = False
			elif event.key == K_d:
				keys[3] = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			shoot.play()
			position = pygame.mouse.get_pos()
			acc[1] += 1
			arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
	
	#12 Move the player	
	if keys[0]:            # w key
		playerpos[1] -= 5
	elif keys[2]:  	       # s key
		playerpos[1] += 5
	elif keys[1]:
		playerpos[0] -= 5
	elif keys[3]:
		playerpos[0] += 5

	#13 Win/Lose check
	if pygame.time.get_ticks() >= 90000:
		running = 0
		exitcode = 1
	if healthvalue <= 0:
		running = 0
		exitcode = 0
	if acc[1]!=0:
		accuracy = acc[0]*1.0/acc[1]*100
	else:
		accuracy=0

#14 Win/Lose Display

if exitcode == 0:
	pygame.font.init()
	font = pygame.font.Font(None,24)
	text = font.render("Accuracy: "+ str(accuracy)+"%",True,(255,0,0))
	textRect = text.get_rect()
	textRect.centerx = screen.get_rect().centerx
	textRect.centery = screen.get_rect().centery+24
	screen.blit(gameover, (0,0))
	screen.blit(text, textRect)
else:
	pygame.font.init()
	font = pygame.font.Font(None,24)
	text = font.render("Accuracy: "+ str(accuracy)+"%",True,(0,255,0))
	textRect = text.get_rect()
	textRect.centerx = screen.get_rect().centerx
	textRect.centery = screen.get_rect().centery+24
	screen.blit(youwin, (0,0))
	screen.blit(text, textRect)	
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
	pygame.display.flip()
