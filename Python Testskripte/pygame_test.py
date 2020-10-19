import os
import random
import pygame
from pygame.locals import * # Constants
import math
import sys

os.environ["SDL_VIDEO_CENTERED"] = "1"

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("LEVEL 2 = Find the Correct Square!")

clock = pygame.time.Clock()

class Player(object):
    def __init__(self):
        self.font_48 = pygame.font.SysFont(None, 48)
        self.font_24 = pygame.font.SysFont(None, 24)

        self.rect = pygame.draw.rect(screen, (0, 0, 128), (100, 100, 100, 100))
        
        self.dist = 10
        self.WHITE =     (255, 255, 255)
        self.BLUE =      (  0,   0, 255)
        self.GREEN =     (  0, 255,   0)
        self.RED =       (255,   0,   0)
        self.TEXTCOLOR = (  0,   0,  0)

    def handle_keys(self):
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit(); exit()
            elif e.type == KEYDOWN:
                key = e.key
                if key == K_LEFT:
                    
                    self.draw_rect(-1, 0)
                elif key == K_RIGHT:
                    self.draw_rect(1, 0)
                elif key == K_UP:
                    self.draw_rect(0, -1)
                elif key == K_DOWN:
                    self.draw_rect(0, 1)
                elif key == K_ESCAPE:
                    pygame.quit(); exit()

    def draw_rect(self,x,y):
        screen.fill((255, 255, 255))
        self.rect = self.rect.move(x*self.dist, y*self.dist); pygame.draw.rect(screen, (0, 0, 128), self.rect)
        #self.draw_circle(screen)
        pygame.display.update()

    def draw(self, surface):
        pygame.draw.rect(screen, (0, 0, 128), (64, 54, 16, 16))

    def draw_circle(self,surface):
        for i in range(15,585,30):
            for j in range(15,585,30):
                self.P11 = pygame.draw.circle(screen, self.BLUE, (i,j), 10)
    
    def draw_TEXT(self,Text):
        img = self.font_24.render(Text ,True, self.BLUE)
        screen.blit(img, (100, 100))



pygame.init()

player = Player()
#clock = pygame.time.Clock()
screen.fill((255, 255, 255))
player.draw(screen)
player.draw_TEXT("")
pygame.display.update()

while True:
  player.handle_keys()
