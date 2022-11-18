#!/usr/bin/env python3
from isi.isi import isi
from operators import sweeper, window, WOp
import cv2 as cv
import sys
import os
import numpy as np    


def count(orig, target, brush, oc_tot, oc_set):

    im_o = cv.imread(orig, cv.IMREAD_GRAYSCALE)        
    _, im_o = cv.threshold(im_o, 127, 255, cv.THRESH_BINARY)
    im_t = cv.imread(target, cv.IMREAD_GRAYSCALE)        
    _, im_t = cv.threshold(im_t, 127, 255, cv.THRESH_BINARY)

    sw = sweeper(brush, im_o)
    L, C = (im_o.shape[0], im_o.shape[1])

    for l in range(L):
        for c in range(C):
            bt = sw.get_bitset((l, c))
            if not (bt in oc_tot):
                oc_tot[bt]=0
                oc_set[bt]=0
            oc_tot[bt] += 1
            if im_t[l][c]:
                oc_set[bt] += 1
    

def main():
    wd = window([(0,-1), (0, 1), (-1, 0), (1, 0), (0, 0)]);
    orig_dir = sys.argv[1]
    target_dir = sys.argv[2]    
    wd_file = sys.argv[3]
    
    orig_l = sorted([orig_dir +'/'+ f for f in os.listdir(orig_dir)])
    target_l = sorted([target_dir + '/' + f for f in os.listdir(target_dir)])
    window_list=[]   
    with open(wd_file) as brf:               
        l = brf.readline()    
        while len(l) > 1:
            pos = [int(p_i) for p_i in l.split()]
            window_list.append(pos)
            l = brf.readline()    

    wd = window(window_list)
    N= int(sys.argv[4])
    oc_tot={}
    oc_set={}
    ind=(np.random.rand(N) * len(orig_l)).astype(int)
    for j in range(len(ind)): 
        i = ind[j]
        print(f"Processing {orig_l[i]} and {target_l[i]}", file=sys.stderr)
        count(orig_l[i], target_l[i], wd, oc_tot, oc_set)    
    true=[]
    false=[]
    
    for key in oc_tot:
        if oc_set[key]/oc_tot[key] > 0.5:
            true.append(key)
        else:
            false.append(key)

    print("Splitting intervals...", file=sys.stderr)
    it_l = isi(true, false, len(wd))
    
    for it in it_l:
        print(it)
    print()
    print(wd)

if __name__ == "__main__":
    main()
        