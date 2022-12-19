
from network import NN
from network_bool import NN_b
from operators.bitset import *
import cv2 as cv
import numpy as np
import torch

class window:
    def __init__(self, pos_l):
        # o que é pos_l ?
        self.pos_l=pos_l;

    def __len__(self):
        return len(self.pos_l)

    def __str__(self):
        ret= ''
        for p in self.pos_l:
            ret += f'{p[0]} {p[1]}\n'
        return ret

class sweeper:
    def __init__(self, brush, img):
        self.brush = brush
        self.img = img

    def get_bitset(self, pos):
        res = bitset(0, len(self.brush))
        for i in range(len(self.brush)):
            p = self.brush.pos_l[i]
            c_pos = (p[0] + pos[0], p[1] + pos[1])
            if c_pos[0] >= 0 and c_pos[0] < self.img.shape[0] and c_pos[1] >= 0 and c_pos[1] < self.img.shape[1] and self.img[c_pos[0], c_pos[1]] != 0:
                res[i] = True
        return res

class WOp:
    def __init__(self, window):
        # o que é brush?
        self.window = window
        self.nn = NN()
        self.nn.load_state_dict(torch.load('model.st'))
        self.nn.eval()

    def apply(self, im):        
        # im = janela
        sw = sweeper(self.window, im)
        # tamanho da imagem
        (L, C) = im.shape
        # imagem resultado
        res = np.ndarray((L, C))
        # percorre posições da imagem
        for l in range(L):
            for c in range(C):
                bt = sw.get_bitset((l, c))
                bt_l = [bt[i] * 1 for i in range(len(bt))]
                with torch.no_grad():
                    nn_out = self.nn(torch.Tensor(bt_l))
                maximum = torch.argmax(nn_out).item()
                res[l,c] = maximum * 255

        return res
            


class WOp_b:
    def __init__(self, window):
        # o que é brush?
        self.window = window
        self.nn = NN_b()
        self.nn.load_state_dict(torch.load('model_bool.st'))
        self.nn.eval()

    def apply(self, im):        
        # im = janela
        sw = sweeper(self.window, im)
        # tamanho da imagem
        (L, C) = im.shape
        # imagem resultado
        res = np.ndarray((L, C))
        # percorre posições da imagem
        for l in range(L):
            for c in range(C):
                bt = sw.get_bitset((l, c))
                bt_l = [bt[i] * 1 for i in range(len(bt))]
                with torch.no_grad():
                    nn_out = self.nn(torch.Tensor(bt_l))
                maximum = nn_out.item() > 0.5
                res[l,c] = maximum * 255

        return res


