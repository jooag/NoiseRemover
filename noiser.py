#!/usr/bin/env python3
import cv2 as cv
import numpy as np
import sys
import os

def main():
    indir=sys.argv[1]
    outdir=sys.argv[2]
    files = sorted([indir +'/'+ f for f in os.listdir(indir)])
    for f in files:
        print(f)
        im = cv.imread(f, cv.IMREAD_GRAYSCALE)
        
        ret, im = cv.threshold(im, 127, 255, cv.THRESH_BINARY)
        
        N = im.shape[0] * im.shape[1]
        
        cv.imwrite(f, im)
        f=f[f.rfind('/')+1:]        
        n_salt = np.random.randint(0, N//15)
        n_pepper = np.random.randint(0, N//15)

        for _ in range(n_salt):
            l = np.random.randint(0, im.shape[0])
            c = np.random.randint(0, im.shape[1])
            im[l][c] = 255

        for _ in range(n_pepper):
            l = np.random.randint(0, im.shape[0])
            c = np.random.randint(0, im.shape[1])
            im[l][c] = 0

        outf = outdir + '/' + f
        print(outf)
        cv.imwrite(outf, im)

if __name__ == "__main__":
    main()