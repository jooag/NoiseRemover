#!/usr/bin/env python3

import numpy as np
import sys
import os

def main():
    trainf=sys.argv[1]
    testf=sys.argv[2]
    n_train = int (sys.argv[3])
    n_test = int (sys.argv[4])
    noise = float (sys.argv[5])
    w=np.array([0.3,-0.5, 0.01 , 2, -2])
    with open(trainf, "w+") as file:
        for i in range(n_train):
            age = np.random.random()
            gender = np.sign(np.random.random() - 0.5)
            salary = np.random.random()
            debt = np.random.random()
            x=np.array([1, age, gender, salary, debt])
            y = np.sign(w.dot(x))
            if np.random.random() <= noise:
                y = -1 * y
            file.write(f"{age*70 + 18} {gender} {salary*100000} {debt*100000} {y}\n")

    with open(testf, "w+") as file:
        for i in range(n_test):
            age = np.random.random()
            gender = np.sign(np.random.random())/2 + 1
            salary = np.random.random()
            debt = np.random.random()
            x=np.array([age, gender, salary, debt])           
            file.write(f"{age*70 + 18} {gender} {salary*100000} {debt*100000} \n")
        



       
        

if __name__ == "__main__":
    main()