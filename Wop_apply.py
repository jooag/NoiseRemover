#!/usr/bin/env python3
import os
import cv2 as cv
from operators import *
from network_bool import NN_b
import sys

def main():        
    it=[]       
    wd = window([(0,-1), (-1, 0), (0, 0), (1, 0), (0, 1)]);
    op = WOp(wd)
    imdir = sys.argv[1]    
    outdir= sys.argv[2]
    im_l = sorted([imdir + '/' + f for f in os.listdir(imdir)])
    
    N=int(sys.argv[3])
    if N > 0:
        ind=(np.random.rand(N) * len(im_l)).astype(int)
    else:
        ind=[int(s) for s in sys.argv[5:]]

    if not os.path.exists(outdir):
        os.makedirs(outdir)

    for i in ind:
        f = im_l[i]
        print(f)
        im_orig = cv.imread(f, cv.IMREAD_GRAYSCALE)
        im_res = op.apply(im_orig)
        cv.imwrite(outdir + '/' + f[f.rfind('/')+1:], im_res)


    

if __name__ == '__main__':
    main()