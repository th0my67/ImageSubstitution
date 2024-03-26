from config import Config
import pygame
import numpy as np
from time import time, mktime, strptime
from numpy import array
from pygame import display, image
from json import load, dump
from module import random_path



def main():
    pygame.init()
    scrn = display.set_mode(Config.SCREEN_SIZE)
    img_1 = pygame.image.load(Config.image1)
    img_2 = pygame.image.load(Config.image2)
    pygame.display.set_caption('substitution images')
    imgarray_1 = pygame.surfarray.pixels2d(img_1)
    imgarray_2 = pygame.surfarray.pixels2d(img_2)



    # On récupère les coordonnées des pixels
    with open(Config.coords_file) as f:
        coords = load(f)


random_path()