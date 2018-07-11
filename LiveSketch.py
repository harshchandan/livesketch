import cv2
import numpy as np


def sketch(image):

    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                           #converts image to grayscale

    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)                         #blurs the image using Gaussian blur

    canny_edges = cv2.Canny(img_gray_blur, 10, 70)                               #finds out edges using Canny

    ret, mask = cv2.threshold(canny_edges, 90, 255, cv2.THRESH_BINARY_INV)       #does binary inversion

    return mask



cap = cv2.VideoCapture(0)                                                        #initializes webcam



while True:

    ret, frame = cap.read()
    cv2.imshow('Live Sketch', sketch(frame))

    if cv2.waitKey(1) == 13:                                                     #closes webcam when Enter key is pressed
        break
        
 

cap.release()
cv2.destroyAllWindows()