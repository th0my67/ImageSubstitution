from numpy import arange, array, copy
from random import shuffle
from config import Config
from json import dump
def random_path():
    x_path = arange(Config.SCREEN_WIDTH//4)
    path = array([copy(shuffle(x_path)) for _ in range(Config.SCREEN_HEIGHT//4)])
    dump(path, Config.coords_file)
    return path

random_path()