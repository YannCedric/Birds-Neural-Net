import pygame
from random import randrange

from Bird import Bird
from Obstacle import Obstacle

WHITE =     (255, 255, 255)
BLUE =      ( 229,255,255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
BLACK = (  0,   0,  0)
(width, height) = (800, 400)

gameDisplay = pygame.display.set_mode((width,height))

pygame.display.set_caption('Game')
birdpic1 = pygame.image.load('birds/bird1.png')
birdpic2 = pygame.image.load('birds/bird2.png')
birdpic3 = pygame.image.load('birds/bird3.png')

birdpics = [birdpic1,birdpic2,birdpic3]

clock = pygame.time.Clock()

birds = []
obstacles = []

pop_size = 100

def generate_population(number, gen_count):
    popu = []
    gen_count = gen_count + 1 
    for i in range(number):
        random_index = randrange(0,len(birdpics))
        popu.append( Bird(height/2, birdpics[random_index]) )
    return popu,gen_count

def generate_obstacle():
    return Obstacle(height, width)

def filterObstacles(obs):
    bye = []
    for o in obs:
        if o.x < 0:
            bye.append(o)
            obs.append(generate_obstacle())
            
    for i in bye:
        obs.remove(i)

    return obs

(birds,gen_count) = generate_population(pop_size, 0)
generations = gen_count
obstacles.append(generate_obstacle())

pygame.font.init()
myfont = pygame.font.SysFont("Arial", 20)  

def updateLabel(val,display):
    lbl = myfont.render('Birds count: '+val, False, (0, 0, 0))
    display.blit(lbl, (10,10))  

def updateLabel2(val,display):
    lbl = myfont.render('Generations count: '+val, False, (0, 0, 0))
    display.blit(lbl, (height-30,10))  


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
        (birds,gen_count) = birds + generate_population(pop_size-len(birds), count)
        count = gen_count

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
        bird.tick(gameDisplay,0,height,obstacles)
    for obs in obstacles:
        obs.tick(gameDisplay)

    (birds,gen_count1) = filterBirds(birds, generations)
    generations = gen_count1
    obstacles = filterObstacles(obstacles)
    
    updateLabel(str(len(birds)),gameDisplay)
    updateLabel2(str(generations), gameDisplay)
    

    if pause == False:
        pygame.display.flip()
    
    if len(birds) < 1:
        (birds, gen_count) = generate_population(pop_size - len(birds),generations)
        generations = gen_count

    gameDisplay.fill(BLUE)
    
pygame.quit()
quit()