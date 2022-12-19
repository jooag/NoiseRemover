import numpy as np

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