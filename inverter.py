#!/usr/bin/env python3
import cv2 as cv
import numpy as np
import sys
import os

def main():
    imdir=sys.argv[1]
    files = sorted([imdir +'/'+ f for f in os.listdir(imdir)])
    for f in files:
        print(f)
        im = cv.imread(f, cv.IMREAD_GRAYSCALE)
        
        ret, im = cv.threshold(im, 127, 255, cv.THRESH_BINARY)         
        
        
        cv.imwrite(f, ~im)
       
        

if __name__ == "__main__":
    main()