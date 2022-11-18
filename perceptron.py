#!/usr/bin/env python3
import numpy as np
import sys 

def main():
    trainf = sys.argv[1]
    testf = sys.argv[2]
    xlist=[]
    ylist = []
    max_iter=int(sys.argv[3])
    with open(trainf) as file:
        l = file.readline()
        while len(l) > 1:
            x=[]
            x.append(1)
            dt = l.split()
            param = dt[:len(dt) - 1]
            ylist.append(float(dt[len(dt) - 1])) 
            for p in param:
                x.append(float(p))
            xlist.append(np.array(x))
            l=file.readline()

    w=np.zeros(xlist[0].shape)            

    max_l=np.copy(xlist[0])

    min_l=np.copy(xlist[0])

    for x in xlist:
        for i in range(len(x)):
            if x[i] <= min_l[i]:
                min_l[i] = x[i]
            if x[i] >= max_l[i]:
                max_l[i] = x[i]
    gap = max_l - min_l
    for x in xlist:
        for i in range(len(x)):
            x[i] -= min_l[i]
            if gap[i] != 0:
                x[i] /= gap[i]

    it= 0
    while it < max_iter:
        found=False
        for i in range(len(xlist)):
            x = xlist[i]
            hx = np.sign(w.dot(x))
            if hx == 0:
                hx = 1
            if hx !=ylist[i]:
                w = w + ylist[i]*x
                found= True
                it+=1
                break;
        if not found:
            break;
    
    xlist=[]
  

    print(w,file=sys.stderr)
    with open(testf) as file:
        l = file.readline()
        while len(l) > 1:
            x=[1]            
            param = l.split()            
            for p in param:
                x.append(float(p))
            xlist.append(np.array(x))
            l=file.readline()
    
    for x in xlist:
        for i in range(len(x)):
            x[i] -= min_l[i]
            if gap[i] != 0:
                x[i] /= gap[i]
        print(f"{np.sign(w.dot(x))}")


        

if __name__ == "__main__":
    main()