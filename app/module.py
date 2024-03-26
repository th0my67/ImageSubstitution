from numpy import array, random
from config import Config
from json import dump
def random_path():
    path = [None] * (Config.SCREEN_HEIGHT * Config.SCREEN_WIDTH)
    for x in range(Config.SCREEN_WIDTH):
        for y in range(Config.SCREEN_HEIGHT):
            path[x * Config.SCREEN_HEIGHT + y] = (x, y)
    random.shuffle(path)
    with open(Config.coords_file, 'w') as f:
        dump(path, f)
    return array(path)
