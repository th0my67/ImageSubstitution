from cv2 import imshow, imread, waitKey
from numpy import array, arange, random
from time import sleep, time, strptime, mktime


old_image = imread("old.jpg")
new_image = imread("new.jpg")


def show_image_transition(old_image, new_image, end_time):

    #Initialisation
    height, width = old_image.shape[:2]
    total_size = height * width

    random_array = array([arange(height) for _ in range(width)])
    for arr in random_array:
        random.shuffle(arr)

    start_time = time()
    end_time = mktime(strptime(end_time, "%d-%m-%y %H:%M:%S"))
    total_duration = end_time - start_time



    

    #Main loop
    y = 0
    while y < height:

        random_x = arange(width)
        random.shuffle(random_x)
        i = 0
        already_done = y*width
        while i < width:
            if ((time() - start_time)/total_duration)*total_size > already_done + i:
                old_image[random_array[random_x[i],y], random_x[i]] = new_image[random_array[random_x[i],y], random_x[i]]
                i += 1
                imshow("Transition", old_image)
                waitKey(1)
            else:
                print("Waiting")
                sleep(1)
        y += 1


show_image_transition(old_image, new_image, "21-02-24 17:25:00")
