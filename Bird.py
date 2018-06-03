import pygame
from Brain import Brain


class Bird: 
    def __init__(self, y, pic):
        self.brain = Brain(6)
        self.x = 30
        self.y = y
        self.speed_y = 0
        self.speed_x = 3
        self.acceleration_y = 9
        self.interval = 0.1
        self.pic = pic
        self.fitness = 0

    def move(self):
        old_pos = self.y
        old_speed_y = self.speed_y
        acceleration_y = self.acceleration_y
        time = self.interval

        self.speed_y = old_speed_y + acceleration_y * time
        self.y = old_pos + old_speed_y*time + acceleration_y*time/2

        # self.x = self.x + self.speed_x

    def jump(self):
        self.speed_y = -30

    def startover(self):
        self.fitness = 0
        self.x = -25

    def think(self,top, bottom, obstacles):

        obstacles_position = []

        for obs in obstacles: 
            obstacles_position.append(obs.x)
            obstacles_position.append(obs.y)

        input = [self.x, self.y , top, bottom]
        input = input + obstacles_position
        prediction = self.brain.feedfoward(input)
        if prediction > 0.6:
            self.jump()

    def draw(self,surface):
        self.fitness = self.fitness + 0.5
        surface.blit(self.pic, (self.x,self.y))
    
    def tick(self, surface, top, bottom, obstacles):
        self.move()
        self.think(top,bottom,obstacles)
        self.draw(surface)
    