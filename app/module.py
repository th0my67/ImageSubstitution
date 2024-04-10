from numpy import array, random
from config import Config
from json import dump
def random_path():
    path_heigth = Config.SCREEN_HEIGHT//3
    path_width = Config.SCREEN_WIDTH//3
    path = [None] * (path_heigth * path_width)
    random_order = random.permutation(path_heigth * path_width)
    for x in range(path_heigth):
        for y in range(path_width):
            path[random_order[x * path_width + y]] = (x*3, y*3)
    with open(Config.coords_file, 'w') as f:
        dump(path, f)
    return array(path)
