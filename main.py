from modules.eye import Eye
import cv2


lefty = Eye()

while True:

    cv2.imshow("Eye", lefty.array())
    cv2.waitKey(1)
