from config import Config
import os
from time import time, mktime, strptime, sleep
from numpy import array
import json
from module import random_path
import cv2



def main():


    imgarray_1 = cv2.imread(os.path.join("images",Config.image1))
    imgarray_2 = cv2.imread(os.path.join("images",Config.image2))

    strt_time = mktime(strptime(Config.start_dt,"%Y-%m-%d %H:%M:%S"))
    duration_constant = (mktime(strptime(Config.end_dt,"%Y-%m-%d %H:%M:%S")) - strt_time)/(Config.SCREEN_HEIGHT * Config.SCREEN_WIDTH / Config.Cross_length / Config.Cross_height)
    uptade_frequency = 1/Config.desired_fps


    cv2.namedWindow('image', cv2.WINDOW_NORMAL)



    cv2.imshow('image', imgarray_1)
    cv2.waitKey(0)



    try:
        with open(Config.coords_file) as f:
            path = array(json.load(f))
            print('path loaded')
            
    except:
        path = random_path()

    current_pos = 0 #int((time() - strt_time) * duration_constant)
    last_time = time()
    for (x ,y) in path[current_pos:]:
        imgarray_1[x - 1:x + 2, y] = imgarray_2[ x - 1:x + 2 , y]
        imgarray_1[x, y - 1 :y + 2 ] = imgarray_2[x, y - 1 :y + 2]
        
        sleep(0.0001)
        if time() - last_time > uptade_frequency:
            last_time = time()
            cv2.imshow('image', imgarray_1)
            cv2.waitKey(1)

    imgarray_1[0:3, : ] = imgarray_2[0:3, : ]
    imgarray_1[-3:, : ] = imgarray_2[-3:, : ]
    imgarray_1[:, 0:3] = imgarray_2[:, 0:3]
    imgarray_1[:, -3:] = imgarray_2[:, -3:]

    for (x ,y) in path[current_pos:]:
        if x+1 < Config.SCREEN_HEIGHT and y-1 < Config.SCREEN_WIDTH:
            imgarray_1[x - 2 : x, y + 1 : y + 3] = imgarray_2[ x - 2 : x, y + 1 : y + 3]
        #else:
            #if x - 1 > 0 and y+2 < Config.SCREEN_WIDTH:
            #    imgarray_1[x - 1, y + 2] = imgarray_2[ x - 1, y + 2]
        
        sleep(0.0001)
        if time() - last_time > uptade_frequency:
            last_time = time()
            cv2.imshow('image', imgarray_1)
            cv2.waitKey(1)
     

    cv2.imshow('image', imgarray_1)
    cv2.waitKey(0)
    
main()