#!/usr/bin/env python3
import numpy as np
import sys 

def main():
    
    testdata = sys.argv[1]
    testres = sys.argv[2]
    xlist=[]
    with open(testdata) as file:
        l = file.readline()
        while len(l) > 1:
            x=[1]            
            param = l.split()            
            for p in param:
                x.append(float(p))
            xlist.append(np.array(x))
            l=file.readline()
    w=np.array([0.3,-0.5, 0.01 , 2, -2])
    ylist=[]
    for x in xlist:
        x -=[0, 18, -1, 0, 0]
        x /=[1, 70, 2, 100000, 100000]
        ylist.append(np.sign(w.dot(x)))
    total = len(xlist)
    correct = 0
    with open(testres) as file:
        l = file.readline()
        i = 0
        while len(l) > 1:            
            param = l.split()            
            if (float(param[0])) == ylist[i]:
                correct += 1
            l=file.readline()
            i += 1
    print(f"{correct/total}")


        

if __name__ == "__main__":
    main()