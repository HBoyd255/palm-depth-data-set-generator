from modules.vision import Vision
import cv2


eyes = Vision()

while True:

    cv2.imshow("Both Feeds", eyes.joined_array())
    cv2.imshow("Overlay", eyes.onion_array())

    cv2.waitKey(1)
