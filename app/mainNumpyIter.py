from cv2 import imshow, imread, waitKey
from numpy import array, arange, random, nditer
from time import sleep, time, strptime, mktime, perf_counter_ns


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

    size_per__duration = total_size/total_duration


    

    #Main loop
    
    for y in range(height):

        random_x = arange(width)
        random.shuffle(random_x)
        already_done = y*width

        x = nditer(random_x, flags=["f_index"])

        strt1 = perf_counter_ns()

        while not x.finished:
            total=0
            strt2 = perf_counter_ns()
            if (time() - start_time) * size_per__duration > already_done + x.index:
                old_image[random_array[x[0],y], x[0]] = new_image[random_array[x[0],y], x[0]]
                x.iternext()
                imshow("Transition", old_image)
                waitKey(1)
                nd2 = perf_counter_ns()
                total += nd2 - strt2

            else:
                print("Waiting")
                sleep(1)
        print(total/width)
        nd1 = perf_counter_ns()
        print(nd1 - strt1)


show_image_transition(old_image, new_image, "23-02-24 10:58:00")
