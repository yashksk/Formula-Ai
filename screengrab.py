import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey, ReleaseKey, W, A, S, D

for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

print('press')
PressKey(W)
time.sleep(3)
print('release')
ReleaseKey(W)


def process_img(image):
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Turns the image gray
    processed_img = cv2.Canny(processed_img, threshold1=100, threshold2=200)
    # Canny edge detection algorithm
    return processed_img

# last_time = time.time()
# while(True):
#     screen = np.array(ImageGrab.grab(bbox=(0,40,1280,750)))
#     new_screen = process_img(screen)

#     print('{} seconds'.format(time.time()-last_time))
#     last_time = time.time()
#     cv2.imshow('window', new_screen)
#     #cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
#     # Converting color from BGR to RGB
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break