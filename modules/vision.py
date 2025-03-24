import cv2
import numpy
from modules.eye import Eye


class Vision:

    def __init__(self):

        self.left = Eye("Left")
        self.right = Eye("Right")

    def both_arrays(self):
        return self.left.array(), self.right.array()

    def joined_array(self):
        joined = numpy.hstack((self.left.array(), self.right.array()))
        return joined

    def onion_array(self):
        onion = cv2.addWeighted(
            self.left.array(), 0.5, self.right.array(), 0.5, 0
        )

        return onion
