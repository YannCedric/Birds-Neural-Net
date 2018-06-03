import pygame

class Bird: 
    def __init__(self, y):
        self.x = 20
        self.y = y
        self.speed_y = -20
        self.acceleration_y = 9
        self.interval = 0.1
        self.pic = pygame.image.load('bird.png')

    def move(self):
        old_pos = self.y
        old_speed_y = self.speed_y
        acceleration_y = self.acceleration_y
        time = self.interval

        self.speed_y = old_speed_y + acceleration_y * time
        self.y = old_pos + old_speed_y*time + acceleration_y*time/2

    def jump(self):
        self.speed_y = -30

    def draw(self,surface):
        surface.blit(self.pic, (self.x,self.y))