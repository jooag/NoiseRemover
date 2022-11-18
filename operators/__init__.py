from isi.isi import bitset, interval, isi
import cv2 as cv
import numpy as np


class window:
    def __init__(self, pos_l):
        self.pos_l=pos_l;

    def __len__(self):
        return len(self.pos_l)

    def __str__(self):
        ret= ''
        for p in self.pos_l:
            ret += f'{p[0]} {p[1]}\n'
        return ret

class sweeper:
    def __init__(self, brush, img):
        self.brush = brush
        self.img = img

    def get_bitset(self, pos):
        res = bitset(0, len(self.brush))
        for i in range(len(self.brush)):
            p = self.brush.pos_l[i]
            c_pos = (p[0] + pos[0], p[1] + pos[1])
            if c_pos[0] >= 0 and c_pos[0] < self.img.shape[0] and c_pos[1] >= 0 and c_pos[1] < self.img.shape[1] and self.img[c_pos[0], c_pos[1]] != 0:
                res[i] = True
        return res

class WOp:
    def __init__(self, brush, intervals):
        self.brush = brush
        self.intervals = intervals


    def apply(self, im):        
        sw = sweeper(self.brush, im)
        (L, C) = im.shape
        res = np.ndarray((L, C))
        for l in range(L):
            for c in range(C):
                bt = sw.get_bitset((l, c))
                isSet = False
                for i in range(len(self.intervals)):
                    it = self.intervals[i]                
                    if(bt in it):
                        res[l, c] = 255
                        isSet=True
                        break;
                if not isSet:
                    res[l, c] = 0
        return res
                


