import pygame
import random
from Brain import Brain

BLACK = (  0,   0,  0)

class Obstacle: 
    def __init__(self, height, x):
        gap = 100
        self.y = random.randint(gap,height)
        self.height = height
        # self.y = height/2
        self.speed_x = -3
        self.x = x

    def move(self):
        self.x = self.x + self.speed_x

    def draw(self,surface):
        thiccness = 100
        pygame.draw.rect(surface,BLACK, (self.x,self.y,thiccness,self.height))

    def tick(self, surface):
        self.move()
        self.draw(surface)
    