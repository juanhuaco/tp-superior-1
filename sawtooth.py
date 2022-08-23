from scipy.fftpack import fft
import scipy as scp
import matplotlib.pyplot as plt
import numpy as np
import sympy as smp

# Number of sample points
N = 600
# sample spacing
T = 1.0 / 800.0

x = smp.symbols('x', real=True)

y = scp.signal.sawtooth(2 * np.pi * 5 * x, width=.5)
yf = fft(y)
xf = np.linspace(0.0, 1.0 / (2.0*T), N//2)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.show() 