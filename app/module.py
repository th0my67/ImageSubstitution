from numpy import array, random
from config import Config
from json import dump
def random_path():
    path_heigth = Config.SCREEN_HEIGHT//3 + 1
    path_width = Config.SCREEN_HEIGHT//3 + 1
    path = [None] * (path_heigth * path_width)
    for x in range(path_heigth):
        for y in range(path_width):
            path[x * Config.SCREEN_HEIGHT + y] = (x*3, y*3)
    random.shuffle(path)
    with open(Config.coords_file, 'w') as f:
        dump(path, f)
    return array(path)
