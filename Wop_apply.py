#!/usr/bin/env python3
import os
import cv2 as cv
from isi import *
from operators import *
import sys

def main():    
    op_file=sys.argv[1]
    it=[]
    window_list=[]  
    with open(op_file) as opf:
        
        l=opf.readline()
        while len(l) > 1:
            it_s = l.split()
            it.append(interval(bitset(it_s[0]), bitset(it_s[1])))
            l = opf.readline()      
        
              
        l = opf.readline()    
        while len(l) > 1:
            pos = [int(p_i) for p_i in l.split()]
            window_list.append(pos)
            l = opf.readline()    
        
    wd = window(window_list)
    op = WOp(wd, it)
    imdir = sys.argv[2]    
    outdir= sys.argv[3]
    im_l = sorted([imdir + '/' + f for f in os.listdir(imdir)])
    
    N=int(sys.argv[4])
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