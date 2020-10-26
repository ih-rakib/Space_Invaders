import math
import random
import pygame
from pygame import mixer
pygame.init()
clock = pygame.time.Clock()
#Background
background = pygame.image.load('background.jpeg')
#Background Music

#Create game window
screen = pygame.display.set_mode((600,1300))
#Enemy
enemy = []
enemy_x = []
enemy_y = []
num = 7
move_direction = []
move1_direction = []
for i in range(num):
	enemy.append(pygame.image.load('enemy1.png'))
	enemy_x.append(random.randint(0,590))
	enemy_y.append(random.randint(90,900))
	move_direction.append(i)
	move1_direction.append(i)
	
#Spaceship
space_invaders = pygame.image.load('space_invaders1.png')

#Bullet
bullet = pygame.image.load('bullet.png')
fired = False
bullet_y = 1270
bullet_x = 349

#Score
score = 0
font = pygame.font.Font('freesansbold.ttf',40)
text_X = 40
text_Y = 60

#Game Over text
gameover = pygame.font.Font('freesansbold.ttf',70)

y_score = pygame.font.Font('freesansbold.ttf',47)

#Author
author = pygame.font.Font('freesansbold.ttf',40)
name_x = 540
name_y = 60
def show_score(x,y):
	val = font.render("Score : " + str(score),True,(255,255,255))
	screen.blit(val,(x,y))

def game_over():
	game = gameover.render("GAME OVER",True,(0,255,0))
	screen.blit(game,(150,600))

def name(x,y):
	name = author.render("®Rakib",True,(255,255,255))
	screen.blit(name,(name_x,name_y))
	
def result():
	res = y_score.render("Your Score : " + str(score),True,(255,255,255))
	screen.blit(res,(200,690))
			
def enemy_func(x,y,i):
	screen.blit(enemy[i],(x,y))
	
def isCollision(enemy_x,enemy_y,bullet_x,bullet_y):
	distance = math.sqrt((math.pow(enemy_x-bullet_x,2))+(math.pow(enemy_y-bullet_y,2)))	
	if distance < 95:
		return True
	else:
		return False	

#create an infinite loop
keep_alive = True
while keep_alive:
    screen.fill((0,0,0))
    #Background image
    screen.blit(background,[0,0])  

    #Check whether it’s the space key press
    for e in pygame.event.get():
    	if e.type==pygame.KEYDOWN:
    		fired = True  		
    	elif e.type==pygame.MOUSEBUTTONDOWN:    		
    		fired = True
    		gun = mixer.Sound('gun1.mp3')
    		gun.play()
    
    #Add Enemy animation logic here
    for i in range(num):
    	#Game Over
    	if enemy_y[i] >= 1125:
    		for j in range(num):
    			enemy_y[j] = 3000
    			
    		game_over()
    		fired = False
    		result()
    		break
    	
    	if move_direction[i] == 'right':
        	enemy_x[i] = enemy_x[i] + 3
        	if enemy_x[i] >= 590:        	   	
            	  enemy_x[i] = 590
            	  move1_direction[i] = 'down'
            	  enemy_y[i] = enemy_y[i] + 100
            	  move_direction[i] = 'left'
    	else:
        	enemy_x[i] = enemy_x[i] - 3
        	if enemy_x[i] <= 0:        	   	
            	  enemy_x[i] = 0
            	  move1_direction[i] = 'down'
            	  enemy_y[i] = enemy_y[i] + 100
            	  move_direction[i] = 'right'   
            	             	  	 
	 #Collision 
    	collision = isCollision(enemy_x[i],enemy_y[i],bullet_x,bullet_y)
    	if collision:
    		explosion = mixer.Sound('explosion.wav')
    		explosion.play()
    		bullet_y = 1250
    		fired = False
    		score = score + 1
    		enemy_x[i] = random.randint(0,590)
    		enemy_y[i] = random.randint(90,900)    
    	enemy_func(enemy_x[i],enemy_y[i],i)
		         
    # Add bullet animation logic here
    if fired is True:
           bullet_y = bullet_y - 5
           if bullet_y == 50:
               fired = False
               bullet_y = 1250      		
               		
    #Create all screen here
   
    screen.blit(bullet, [bullet_x, bullet_y])
    screen.blit(space_invaders, [300,1250]) 
    
    name(name_x,name_y)
    show_score(text_X,text_Y)
    pygame.display.update()
    clock.tick(110)
