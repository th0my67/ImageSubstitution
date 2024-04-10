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
    total_duration = (mktime(strptime(Config.end_dt,"%Y-%m-%d %H:%M:%S")) - strt_time)

    total_changes = Config.SCREEN_HEIGHT * Config.SCREEN_WIDTH / Config.cross_width / Config.cross_height
    uptade_frequency = 1/Config.desired_fps

    cross_change_speed = total_changes / total_duration / Config.dot_time_proportion * 100
    cross_entire_duration = total_duration * Config.dot_time_proportion / 100

    dot_change_speed = total_changes / total_duration / (100 - Config.dot_time_proportion) * 100


    cv2.namedWindow(Config.WINDOW_NAME, cv2.WINDOW_NORMAL)

    cv2.imshow(Config.WINDOW_NAME, imgarray_1)
    cv2.waitKey(1)


    try:
        with open(Config.coords_file) as f:
            path = array(json.load(f))
            
    except:
        path = random_path()

    #Attente du début
    while time() < strt_time:
        sleep(1)
        cv2.imshow(Config.WINDOW_NAME, imgarray_1)
        cv2.waitKey(1)

    #Recommencer au bon endroit
    cross_current_pos = int((time() - strt_time) * cross_change_speed)
    last_time = time()

    #Rattrapage des croix
    for pos_in_list ,(x ,y) in enumerate(path[:cross_current_pos]):

        #Transition
        imgarray_1[x - 1:x + 2, y] = imgarray_2[ x - 1:x + 2 , y]
        imgarray_1[x, y - 1 :y + 2 ] = imgarray_2[x, y - 1 :y + 2]

    #Transition des croix
    for pos_in_list ,(x ,y) in enumerate(path[cross_current_pos:]):

        #Transition
        imgarray_1[x - 1:x + 2, y] = imgarray_2[ x - 1:x + 2 , y]
        imgarray_1[x, y - 1 :y + 2 ] = imgarray_2[x, y - 1 :y + 2]
        
        #Attente
        while pos_in_list + cross_current_pos > (time()-strt_time) * cross_change_speed:
            sleep(0.1)
            if time() - last_time > uptade_frequency:
                last_time = time()
                cv2.imshow(Config.WINDOW_NAME, imgarray_1)
                cv2.waitKey(1)
        
        #Affichage
        if time() - last_time > uptade_frequency:
            last_time = time()
            cv2.imshow(Config.WINDOW_NAME, imgarray_1)
            cv2.waitKey(1)

    #Transition des bords
    imgarray_1[0:3, : ] = imgarray_2[0:3, : ]
    imgarray_1[-3:, : ] = imgarray_2[-3:, : ]
    imgarray_1[:, 0:3] = imgarray_2[:, 0:3]
    imgarray_1[:, -3:] = imgarray_2[:, -3:]

    #Recommencer au bon endroit
    dot_current_pos = int((time() - strt_time - cross_entire_duration) * dot_change_speed)
    if dot_current_pos < 0:
        dot_current_pos = 0
    
    #Rattrapage des points
    for pos_in_list, (x ,y) in enumerate(path[:dot_current_pos]):

        #Transition
        if x+1 < Config.SCREEN_HEIGHT and y-1 < Config.SCREEN_WIDTH:
            imgarray_1[x - 2 : x, y + 1 : y + 3] = imgarray_2[ x - 2 : x, y + 1 : y + 3]


    #Transition des points
    for pos_in_list, (x ,y) in enumerate(path[dot_current_pos:]):

        #Transition
        if x+1 < Config.SCREEN_HEIGHT and y-1 < Config.SCREEN_WIDTH:
            imgarray_1[x - 2 : x, y + 1 : y + 3] = imgarray_2[ x - 2 : x, y + 1 : y + 3]
        #else:
            #if x - 1 > 0 and y+2 < Config.SCREEN_WIDTH:
            #    imgarray_1[x - 1, y + 2] = imgarray_2[ x - 1, y + 2]
        
        #Attente
        while pos_in_list + dot_current_pos > (time() - strt_time - cross_entire_duration) * dot_change_speed :
            sleep(0.1)
            if time() - last_time > uptade_frequency:
                last_time = time()
                cv2.imshow(Config.WINDOW_NAME, imgarray_1)
                cv2.waitKey(1)
        
        #Affichage
        if time() - last_time > uptade_frequency:
            last_time = time()
            cv2.imshow(Config.WINDOW_NAME, imgarray_1)
            cv2.waitKey(1)
     

    cv2.imshow(Config.WINDOW_NAME, imgarray_1)
    cv2.waitKey(0)
    
main()