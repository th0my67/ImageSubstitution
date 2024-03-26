from config import Config
from time import time, mktime, strptime
from numpy import array
from pygame import display, image
from json import load, dump
from module import random_path

def main():
    scrn = display.set_mode(Config.SCREEN_SIZE)
    img_1 = image.load(Config.image1)
    img_2 = image.load(Config.image2)

    # On récupère les coordonnées des pixels
    with open(Config.coords_file) as f:
        coords = load(f)


random_path()