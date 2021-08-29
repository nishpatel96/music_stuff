""" Write the drawing and displaying keys functions in this class"""
import cv2
import numpy as np

class Keys:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.keynote = keynote

    # def nextKey(self):
    #     x2 = self.x + 30 
    #     return x2

class L_key(Keys):
    def drawKey(self, frame):
        k = np.array([[self.x, self.y], [self.x + 56, self.y], 
                       [self.x + 57, self.y + 162], [self.x + 85, self.y + 162],
                       [self.x + 85, self.y + 250], [self.x, self.y + 250]],
                        np.int32)
        cv2.fillPoly(frame,[k.reshape(-1,1,2)], (255, 255 ,255))

class backLKey(Keys):
    def drawKey(self, frame):
        k = np.array([[self.x, self.y], [self.x + 57, self.y], 
                       [self.x + 57, self.y + 250], [self.x - 29, self.y + 250],
                       [self.x - 29, self.y + 162], [self.x, self.y + 162]],
                        np.int32)
        cv2.fillPoly(frame,[k.reshape(-1,1,2)], (255, 255 ,255))

class uKey(Keys):
    def drawKey(self, frame):
        k = np.array([[self.x, self.y], [self.x + 56, self.y], 
                       [self.x + 57, self.y + 162], [self.x + 85, self.y + 162],
                       [self.x + 85, self.y + 250], [self.x - 29, self.y + 250],
                       [self.x - 29, self.y + 162], [self.x, self.y + 162]],
                        np.int32)
        cv2.fillPoly(frame,[k.reshape(-1,1,2)], (255, 255 ,255))

class blackKey(Keys):
    def drawKey(self, frame):
        cv2.rectangle(frame, (self.x, self.y), (self.x + 56, self.y+160), 0, -1)
