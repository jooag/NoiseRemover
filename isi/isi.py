#!/usr/bin/env python3
import numpy as np
from numba import jit

class bitset:    
    def __init__(self, arg, n=0):
        self.n=n
        self.val=0
        if type(arg) is list or arg is np.ndarray:
            n = len(arg)
            for i in range(n):
                if arg[i] == True:
                    self.val = self.val | (1 << i)
        elif type(arg) is str:            
            self.n = len(arg)
            for i in range(self.n):
                if arg[i] == '1':
                    self[i] = True
        else:
            self.val = arg
        
    def __and__(self, other):        
        return bitset(self.val & other.val, self.n)
        
    def __or__(self, other):        
        return bitset(self.val | other.val, self.n)

    def __xor__(self, other):        
        return bitset(self.val ^ other.val, self.n)

    def __invert__(self):
        return bitset(self.val ^ ((1 << (self.n)) - 1), self.n)

    def mask(self, i):
        return bitset(self.val & (1 << (i)), self.n)

    def __getitem__(self, key):
        return self.mask(key).val != 0

    def __setitem__(self, key, val):
        if val:
            self.val |= (1 << key)
        else:
            self.val &= ~((1 << key))

    def __len__(self):
        return self.n

    def __lt__(self, other):
        return (self.val | other.val) == other.val

    def __str__(self):
        return format(self.val, 'b').rjust(self.n, '0')[::-1]

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.val - other.val == 0

    def __le__(self, other):
        return self < other or self == other

    def __hash__(self):
        return self.val

class interval:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __contains__(self, it):
        if type(it) is bitset:
            return self.a <= it  and it <= self.b
        elif type(it) is interval:
            return self.a <= it.a and it.b <= self.b

    def __len__(self):
        return 2**(self.a ^ self.b).bit_count()

    def __str__(self):
        return self.a.__str__() + ' ' + self.b.__str__() 

    def __repr__(self):
        return self.__str__()


def isi(true, false, n):   
    def split(iv, x):
        mx=[]
        a=iv.a
        b=iv.b
        b_minus_a = a ^ b
        sp_1 = b_minus_a & x
        for i in range(len(sp_1)):        
            if not sp_1[i]:
                continue
            mx.append(interval(a, b & ~(sp_1.mask(i))))
        sp_2 = b_minus_a & (~x)
        for i in range(len(sp_2)):
            if not sp_2[i]:
                continue
            mx.append(interval(a | (sp_2.mask(i)), b))
        return mx

    I = [interval(bitset([False]*n, n), bitset([True]*n, n))]

    ret=[]
    
    while len(I) > 0:
        iv = I.pop()  
        redundant=False
        for it in ret:
            if iv in it:
                redundant = True
                break;
        if redundant:
            continue
        valid=True   
        for f in false:
            if f in iv:                
                I.extend(split(iv, f))       
                valid=False
                break;
        if valid:
            useful=False
            for t in true:            
                if t in iv:
                    useful = True
                    break;
            if useful:
                ret.append(iv)
        
    return ret
    
        
def main():
    true=[bitset('111'), bitset('011')]
    false=[bitset('110'), bitset('000')]
    
    print(isi(true, false, 3))

if __name__ == '__main__':
    main()

