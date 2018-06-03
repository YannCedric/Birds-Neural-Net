import pygame
from random import randrange

from Bird import Bird


WHITE =     (255, 255, 255)
BLUE =      ( 229,255,255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
TEXTCOLOR = (  0,   0,  0)
(width, height) = (800, 400)

gameDisplay = pygame.display.set_mode((width,height))

pygame.display.set_caption('Game')
birdpic1 = pygame.image.load('birds/bird1.png')
birdpic2 = pygame.image.load('birds/bird2.png')
birdpic3 = pygame.image.load('birds/bird3.png')

birdpics = [birdpic1,birdpic2,birdpic3]

clock = pygame.time.Clock()

birds = []
pop_size = 20

def generate_population(number):
    popu = []
    for i in range(number):
        random_index = randrange(0,len(birdpics))
        popu.append( Bird(height/2, birdpics[random_index]) )
    return popu

birds = generate_population(pop_size)  

pygame.font.init()
myfont = pygame.font.SysFont("Arial", 20)  

def updateLabel(val,display):
    lbl = myfont.render('Birds count: '+val, False, (0, 0, 0))
    display.blit(lbl, (10,10))  

def updateLabel2(val,display):
    lbl = myfont.render('Generations count: '+val, False, (0, 0, 0))
    display.blit(lbl, (height-30,10))  

generations = 0

def filterBirds(birds,count):
    bye = []
    lap = False
    for bird in birds:
        if bird.y > height or bird.y < 0:
            bye.append(bird)
        elif bird.x > width:
            lap = True
            bird.startover()
            
    for i in bye:
        birds.remove(i)

    if lap:
        count +=  1            
        birds = birds + generate_population(pop_size-len(birds))
    
    return (birds,count)

clock.tick(60)
crashed = False
pause = False
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for bird in birds:
                    bird.tick(gameDisplay,0,height)

    for bird in birds:
        bird.tick(gameDisplay,0,height)

    (birds,generations) = filterBirds(birds, generations)

    updateLabel(str(len(birds)),gameDisplay)
    updateLabel2(str(generations), gameDisplay)
    

    if pause == False:
        pygame.display.flip()
        
    gameDisplay.fill(BLUE)
    
pygame.quit()
quit()