import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey, ReleaseKey, W, A, S, D

def regionOfInterest(img, vertices):
    mask = np.zeros_like(img)
    # creates an array of zeros the size of the image
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    # just shows region of interest by masking the part that's outside the vertices
    return masked

def process_img(image):
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Turns the image gray
    processed_img = cv2.Canny(processed_img, threshold1=100, threshold2=200)
    # Canny edge detection algorithm
    vertices = np.array([[0,650],[0,380], [500, 310], [780,310], [1280, 380], [1280, 650], [960, 450], [320, 450]])
    processed_img = regionOfInterest(processed_img,[vertices])
    return processed_img

last_time = time.time()
while(True):
    screen = np.array(ImageGrab.grab(bbox=(0,40,1280,750)))
    new_screen = process_img(screen)
    # print('press')
    # PressKey(W)
    # time.sleep(3)
    # print('release')
    # ReleaseKey(W)
    print('{} seconds'.format(time.time()-last_time))
    last_time = time.time()
    cv2.imshow('window', new_screen)
    #cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    # Converting color from BGR to RGB
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break