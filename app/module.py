from numpy import arange, array, copy
from random import shuffle
from config import Config
from json import dump
def random_path():
    x_path = arange(Config.SCREEN_WIDTH//2)
    path = array([copy(shuffle(x_path)) for _ in range(Config.SCREEN_HEIGHT//2)])
    with open(Config.coords_file, 'w') as f:
        dump(path.tolist(), f)
    return path
        
