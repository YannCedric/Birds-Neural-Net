import pygame
from Bird import Bird


WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
TEXTCOLOR = (  0,   0,  0)
(width, height) = (800, 400)

gameDisplay = pygame.display.set_mode((width,height))

pygame.display.set_caption('Game')
birdpic = pygame.image.load('bird.png')
clock = pygame.time.Clock()

crashed = False
bird = Bird(50)

# y = 50
# pygame.draw.circle(gameDisplay, BLUE, (50,50), 10)

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    pygame.display.update()
    clock.tick(60)
    gameDisplay.fill(WHITE)
    bird.move()
    bird.draw(gameDisplay)
    # clock.tick(40)
    # gameDisplay.blit(birdpic, (20,y))
    # pygame.draw.circle(gameDisplay, BLUE, (50,y), 10)   
    # y=y+1
    
pygame.quit()
quit()