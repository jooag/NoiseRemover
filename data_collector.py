#!/usr/bin/env python3
from operators import sweeper, window
import cv2 as cv
import pandas as pd
import sys
import os
import numpy as np    


def count(orig, target, window, data):
    N= 100
    
    im_o = cv.imread(orig, cv.IMREAD_GRAYSCALE)        
    _, im_o = cv.threshold(im_o, 127, 255, cv.THRESH_BINARY)
    im_t = cv.imread(target, cv.IMREAD_GRAYSCALE)        
    _, im_t = cv.threshold(im_t, 127, 255, cv.THRESH_BINARY)

    sw = sweeper(window, im_o)
    L, C = (im_o.shape[0], im_o.shape[1])

    for _ in range(N):
        l = round(np.random.uniform(0.2*L, 0.8*L))
        c = round(np.random.uniform(0.2*C, 0.8*C))
        bt = sw.get_bitset((l, c))
        row={"top": int(bt[0]), "mid-left": int(bt[1]), "mid": int(bt[2]), "mid-right": int(bt[3]), "bot": int(bt[4]), "target": int(im_t[l][c]/255)}
        data.append(row)
   
    

def main():
    wd = window([(0,-1), (-1, 0), (0, 0), (1, 0), (0, 1)]);
    orig_dir = 'img/noise/orig'
    target_dir = 'img/noise/target'   
    
    
    orig_l = sorted([orig_dir +'/'+ f for f in os.listdir(orig_dir)])
    target_l = sorted([target_dir + '/' + f for f in os.listdir(target_dir)]) 
  
    data=[]    
    
    for i in range(min(len(orig_l), len(target_l))): 
        print(f"Processing {orig_l[i]} and {target_l[i]}", file=sys.stderr)
        count(orig_l[i], target_l[i], wd, data)

    df = pd.DataFrame(data)    

    df.to_csv("data.csv", index=False)
    
if __name__ == "__main__":
    main()
        