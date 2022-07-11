import pygame
import random
from sys import exit

##creates window
pygame.init()
width = 760
height = 760
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SNAKE")
clock = pygame.time.Clock()


##scoring
pygame.font.init()
font = pygame.font.SysFont("Dubai Medium", 100)
score = 0

##snake info
snakeposx = [7,8,9]
snakeposy = [9,9,9]
newtail = False
direction = "right"

##generates chequered grid
grid = [[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,],
        [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,],
        [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,],
        [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,],
        [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,],
        [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,],
        [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,],
        [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,],
        [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,],
        [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,],
        [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,],
        [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,],
        [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,],
        [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,],
        [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,],
        [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,],
        [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,],
        [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,],
        [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,]]

##creates surface for grid squares
gsquarew = 40
gsquareh = 40
surface = pygame.Surface((gsquarew,gsquareh))
surface.fill((0, 204, 0))
gwidth = len(grid)
gheight = len(grid[0])

##apple
appleposx, appleposy = 13, 9

playing = True
##game loop
while True:
    
    ##bg colour
    screen.fill((0, 153, 0))

    ##inserts surfaces for each grid square
    for row in range(gwidth):
        for collumn in range(gheight):
            if grid[row][collumn] == 1:
                screen.blit(surface, (gsquarew*collumn, gsquareh*row))

    ##events
    for event in pygame.event.get():

        ##detects exit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        ##detects key presses and prepares next direction change
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and snakeposy[-2] != snakeposy[-1]-1:
                direction = "up"
            if event.key == pygame.K_s and snakeposy[-2] != snakeposy[-1]+1:
                direction = "down"
            if event.key == pygame.K_a and snakeposx[-2] != snakeposx[-1]-1:
                direction = "left"
            if event.key == pygame.K_d and snakeposx[-2] != snakeposx[-1]+1:
                direction = "right"

    ##snake collision
    for i in range(len(snakeposx)-2):
        if snakeposx[-1] == snakeposx[i] and snakeposy[-1] == snakeposy[i]:
            pygame.quit()
            exit()

    if snakeposx[-1] < 0 or snakeposx[-1] > 18:
        pygame.quit()
        exit()
    if snakeposy[-1] < 0 or snakeposy[-1] > 18:
        pygame.quit()
        exit()

    ##appends snake list with new head and removes tail (movement) 
    if direction == "up":
        snakeposx.append(snakeposx[-1])
        snakeposy.append(snakeposy[-1]-1)

    if direction == "down":
        snakeposx.append(snakeposx[-1])
        snakeposy.append(snakeposy[-1]+1)

    if direction == "left":
        snakeposx.append(snakeposx[-1]-1)
        snakeposy.append(snakeposy[-1])

    if direction == "right":
        snakeposx.append(snakeposx[-1]+1)
        snakeposy.append(snakeposy[-1])
        
    snakeposx.pop(0)
    snakeposy.pop(0)

    ##draws snake
    for x in range(len(snakeposx)):
        snake = pygame.Rect(snakeposx[x]*40, snakeposy[x]*40, gsquarew, gsquareh)
        if x == len(snakeposx)-1:
            pygame.draw.rect(screen, ((102, 0, 204)), snake)
        else:
            pygame.draw.rect(screen, ((153, 51, 255)), snake)

    ##detects apple collection
    if snakeposx[-1] == appleposx and snakeposy[-1] == appleposy:
        newapple = True
        newtail = True
        newtailposx = snakeposx[0]
        newtailposy = snakeposy[0]
        while newapple:
            appleposx = random.randint(0,gwidth-1)
            appleposy = random.randint(0,gheight-1)
            
            if appleposx not in snakeposx and appleposy not in snakeposy:
                newapple = False

    ##adds new tail when apple collected
    if newtail == True:
        snakeposx.insert(0, newtailposx)
        snakeposy.insert(0, newtailposy)
        newtail = False
        score += 1

    ##draws apple
    apple = pygame.Rect(appleposx*40, appleposy*40, gsquarew, gsquareh)
    pygame.draw.rect(screen, ("Red"), apple)

    ##score
    text = font.render(f"{score}", False, (0, 0, 0))
    screen.blit(text, (0, -40))
        
    ##refresh
    pygame.display.update()
    clock.tick(5)
