import pygame
import random
from Brain import Brain


class Obstacle: 
    def __init__(self, height):
        self.x = random.randint(0,height)
        self.speed_x = 3
        # self.y = y

    def move(self):
        self.x = self.x + self.speed_x

    def jump(self):
        self.speed_y = -30

    def startover(self):
        self.fitness = 0;
        self.x = 0

    def think(self,top, bottom):
        prediction = self.brain.feedfoward([self.y, top, bottom])
        if prediction > 0.6:
            self.jump()

    def draw(self,surface):
        self.fitness = self.fitness + 0.5
        surface.blit(self.pic, (self.x,self.y))
    
    def tick(self, surface, top, bottom):
        self.move()
        self.think(top,bottom)
        self.draw(surface)
    