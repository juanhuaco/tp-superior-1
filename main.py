from ast import AsyncFunctionDef
import numpy as np
import sympy as smp
import scipy.fft as scp 
from sympy import fft
import matplotlib.pyplot as mpl

def DFT(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    X = np.dot(e, x)
    
    return X

with open("./calamar_pda2.txt") as f:
    contents = f.readlines()
    info = contents[1].split(',')

#===FUNCION ORIGINAL===
info = list(map(lambda e: float(e), info))
N = len(info)
T = 100*N

t = np.linspace(0,T,N)

if False:
    mpl.plot(t, info)
    mpl.show()

print('hello')

#===MUESTRA FUNCION TRANSFORMADA
infodft = DFT(info)
w = scp.fftfreq(len(t), np.diff(t)[0])


if False:
    mpl.plot(w[:N//2], infofft[:N//2])
    mpl.show()

mpl.stem(w, infodft)
mpl.show()

print('bye')