import pygame 
import random
import math


#Initialize pygame
pygame.init()


#Create Screen
screen = pygame.display.set_mode((800,600))  #height and width


#Tittle and Icon
pygame.display.set_caption("Pig Hunter")
icon = pygame.image.load('pig.png')         
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('OG22LT0.jpg')    



#player
playerImg = pygame.image.load('hunter.png')
playerX = 370
playerY = 520
playerX_change = 0

#enemy
enemyImg= []
enemyX =[]
enemyY =[]
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
	enemyImg.append(pygame.image.load('pig64.png'))
	enemyX.append(random.randint(0,735))
	enemyY.append(random.randint(30,200))
	enemyX_change.append(25)
	enemyY_change.append(40)

#bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 370
bulletY = 520
bulletX_change = 0
bulletY_change = 40
bullet_state = 'ready'

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10


def show_score(x, y):
	score = font.render("Score: " + str(score_value), True, (0,0,0))
	screen.blit(score, (x,y))

#Game over
over_font = pygame.font.Font('freesansbold.ttf',64)

def game_over_text():
	over_text = over_font.render("GOODBYE GRU", True, (0,0,0))
	screen.blit(over_text, (150,250))



# Draw 
def player(x,y):
	screen.blit(playerImg, (x,y))

def enemy(x,y,i):
	screen.blit(enemyImg[i], (x,y))

def fire_bullet(x,y):
	global bullet_state 
	bullet_state = "fire"
	screen.blit(bulletImg, (x+16,y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
	distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
	if distance < 35:
		return True
	else:
		return False



#Game loop
running = True 
while running:

	screen.fill((0,128,128))

	#background 
	screen.blit(background, (0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# if key is pressed 
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			playerX_change = -2
		if event.key == pygame.K_RIGHT:
			playerX_change = 2
		if event.key == pygame.K_SPACE:
			if bullet_state is 'ready':

				bulletX = playerX
				fire_bullet(bulletX,bulletY)

	if event.type == pygame.KEYUP:
		if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
			playerX_change = 0

	# Boudaries for player
	playerX += playerX_change

	if playerX <= 0: 
		playerX = 0
	elif playerX >= 736:
		playerX = 736




	# Boudaries for enemy movemnt 
	for i in range(num_of_enemies):
		#Game Over
		if enemyY[i] > 440:
			for j in range(num_of_enemies):
				enemyY[j] = 2000
			game_over_text()
			break


		enemyX[i] += enemyX_change[i]

		if enemyX[i] <= 0: 
			enemyX_change[i] = 15
			enemyY[i] += enemyY_change[i]
		elif enemyX[i] >= 736:
			enemyX_change[i] = -15
			enemyY[i] += enemyY_change[i]

		# Collision
		collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
		if collision:
			bulletY = 480
			bullet_state = 'ready'
			score_value += 1

			enemyX[i] = random.randint(0,735)
			enemyY[i]  = random.randint(30,200)

		enemy(enemyX[i], enemyY[i], i)




	# Bullet Movement
	if bulletY <= 0:
		bulletY = 480
		bullet_state = 'ready'
	if bullet_state is "fire":
		fire_bullet(bulletX, bulletY)
		bulletY -= bulletY_change

	

	player(playerX, playerY)
	show_score(textX, textY)
	pygame.display.update()





