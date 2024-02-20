from cv2 import imshow, imread, waitKey, destroyAllWindows
from numpy import array, arange


old_image = array(imread("old.jpg"))
new_image = imread("new.jpg")


def show_image_transition(old_image, new_image, n_step):
    height, width = old_image.shape[:2]

    for i in range(n_step):
        imshow("Image", old_image)
        waitKey(100)
        old_image[0:720, width // n_step * i : width // n_step * (i + 1)] = new_image[0:720, width // n_step * i : width // n_step * (i + 1)]
    old_image[:, :] = new_image[:, :]
    imshow("Image", old_image)
    waitKey(1)


show_image_transition(old_image, new_image, 100)


old_image[0:240, 0:720] = new_image[0:240, 0:720]
imshow("Image", old_image)


destroyAllWindows()
