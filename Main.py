import pygame
import random
from pygame.locals import *
import time

def changeBackground(img):
    background = pygame.image.load(img)
    bg = pygame.transform.scale(background, (screen_width,screen_height))
    screen.blit(bg,(0,0))

pygame.init()
pygame.display.set_caption('Recycle bin pickup')
screen_width=900
screen_height=700
screen = pygame.display.set_mode([screen_width,screen_height])

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
