from ast import AsyncFunctionDef
import numpy as np
import sympy as smp
import scipy.fft as scp
import matplotlib.pyplot as plt

#open file
with open("./calamar_pda.txt") as f:
    contents = f.readlines()
    info = contents[1].split(',')

#getttt info
info = list(map(lambda e: float(e), info))


#parameters
Fs = 10_000 #sampling freq
tstep = 1 / Fs #sample time interv
N = len(info) #number of samples
fstep = Fs / N #freq interval

#segment graphic
fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1)

#plot original func

t = np.linspace(0, (N-1)*tstep, N)
ax1.plot(t, info)

print('hasta aca todo bien')
#===MUESTRA FUNCION TRANSFORMADA
infofft = np.abs(np.fft.fft(info))
# w = scp.fftfreq(len(t), np.diff(t)[0])
f = np.linspace(0, (N-1)*fstep, N)
if(len(f) == len(infofft)):
    print('bien')
    ax2.plot(f, infofft)
else:
    print('its not working')

plt.show()
