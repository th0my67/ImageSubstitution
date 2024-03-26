from config import Config
import pygame
import numpy as np
from time import time, mktime, strptime
from numpy import array
from json import load, dump
from module import random_path



def main():
    pygame.init()
    scrn = pygame.display.set_mode(Config.SCREEN_SIZE)
    img_1 = pygame.image.load(Config.image1)
    img_2 = pygame.image.load(Config.image2)
    pygame.display.set_caption('substitution images')
    imgarray_1 = pygame.surfarray.pixels2d(img_1)
    imgarray_2 = pygame.surfarray.pixels2d(img_2)

    duration = mktime(strptime(Config.end_dt)) - mktime(strptime(Config.start_dt))


    # On récupère les coordonnées des pixels
    try:
        with open(Config.coords_file) as f:
            path = array(load(f))
            
    except:
        path = random_path()

    
    for (x ,y) in path[current_pos:]:
        imgarray_1[[x - 1:x + 1], y] = imgarray_2[[x - 1:x + 1], y]
        imgarray_1[x, [ y - 1 :y + 1 ]] = imgarray_2[x, [y - 1:y + 1]]
        if condition_afficher:
            scrn.blit(img_1, (0, 0))

    
