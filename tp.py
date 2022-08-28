from functools import reduce
from pkg_resources import yield_lines
from scipy.fft import fft
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

#definir datos
f = open("calamar_pda.txt")

info = f.readlines()

DatosTiempo = info[1]
DatosPotencialMembrana = info[3]

PotencialMembrana = list(map(float, (DatosPotencialMembrana.split(","))))
Tiempo = list(map(float, (DatosTiempo.split(","))))

N = len(PotencialMembrana)
dt = 0.0001
Fs = 1.0 / dt


PMfft = fft(PotencialMembrana)
x = np.linspace(0, dt * N , N)

w = Fs * np.linspace (-1/2, 1/2, N)

#EJERCICIO1
def ejercicio1():

    fig, [ax1Ej1, ax2Ej1] = plt.subplots(nrows=1, ncols=2)
    fig.set_size_inches(13, 6)


    ax1Ej1.plot(x, PotencialMembrana, 1)
    plt.subplot(1,2,1)
    plt.title("Ejercicio 1 - Sin Transformar")
    plt.ylabel("PotencialMembrana [mV]")
    plt.xlabel("Tiempo [ms]")
    plt.grid()
 
    ax2Ej1.plot(w, np.abs(PMfft), 2)
    plt.subplot(1,2,2)
    plt.title("Ejercicio 1 - Transformado")
    plt.ylabel("Amplitud []")
    plt.xlabel("Frecuencia []")
    plt.grid()

    plt.savefig("./imagenes/ej1pic.png")
    plt.show()

    return

### EJERCICIO2
def ejercicio2():
    def escalon(t):
        if(t >= 0):
            return 1
        else:
            return 0

    def getLoma(a, timeStep):
        a = abs(a)

        loma = lambda p:  (escalon(p+a) - escalon(p-a)) / (2*a)

        return loma

    a = 20
    timeStep = 1

    y = np.linspace(-a, a, 2*a + 1)
    f = getLoma(a, timeStep)

    filtered = signal.convolve(PotencialMembrana, list(map(f, y)))

    #plotting
    fig, [ax1Ej2, ax2Ej2] = plt.subplots(nrows=1, ncols=2)
    fig.set_size_inches(13, 6)

    ax1Ej2.plot(filtered)
    plt.subplot(1,2,1)
    plt.title("Ejercicio 2 - Funcion Filtrada")
    plt.grid()

    fvalues = []
    for i in y:
        fvalues.append(f(i))

    ax2Ej2.stem(y, fvalues)
    plt.subplot(1,2,2)
    plt.title("Ejercicio 2 - Funcion Lomo")
    plt.grid()

    plt.show()

    return

#EJERCICIO3
def ejercicio3():
    #definiendo funciones
    b1 = 5
    b2 = 3
    def func1(n, b): return (1.0/b) * np.sinc([n * 1.0 / b])[0]
    def func2(n, b): return (1.0/b) * np.sinc( [ (n * 1.0 - 500) / b] )[0]
    
    #filtramos la se;al con el filtro1
    amplitudFiltro1 = 20
    dominioFiltro1 = np.linspace(-amplitudFiltro1, amplitudFiltro1, amplitudFiltro1*2+1)
    rangoFiltro1 = [func1(i, b1) for i in dominioFiltro1]
    
    funcFiltrada1 = signal.convolve(PotencialMembrana, rangoFiltro1, mode="same")

    #filtramos la se;al con el filtro2
    amplitudFiltro2 = 20
    dominioFiltro2 = np.linspace(-amplitudFiltro2, amplitudFiltro2, amplitudFiltro2*2+1)
    rangoFiltro2 = [func1(i, b2) for i in dominioFiltro2]
    
    funcFiltrada2 = signal.convolve(PotencialMembrana, rangoFiltro2, mode="same")


    #plotting
    #plotting
    fig, ax = plt.subplots(nrows=2, ncols=2)
    fig.set_size_inches(12, 8)

    #plt.figure(1)
    plt.subplot(2,2,1)
    plt.title('Funcion Filtrada por Filtro 1')
    ax[0,0].plot(x, funcFiltrada1)
    plt.grid()


    #Antitransformada
    #antitransformada_escalon = np.fft.ifft(escalon)

    #plt.figure(2)
    plt.subplot(2,2,2)
    plt.title('Filtro 1')
    ax[0, 1].plot(dominioFiltro1, rangoFiltro1)
    plt.grid()
    #plt.xlim([0,1000])

    #Aplicar el filtro a la transformada del Potencial
    #Para aplicarlo hicimos una convolucion, multiplicamos en frecuencia y antitransformamos
    #filtrada = escalon * PMfft
    #plt.figure(3)
    plt.subplot(2,2,3)
    plt.title('Funcion Filtrada por Filtro 2')
    ax[1, 0].plot(x, funcFiltrada2)
    plt.grid()

    #antitransformada_filtrada = np.fft.ifft(filtrada)
    #plt.figure(4)
    plt.subplot(2,2,4)
    plt.title('Filtro 2')
    ax[1,1].plot(dominioFiltro2, rangoFiltro2)
    plt.grid()
    plt.show()

def ejercicio4():
    print("ainda nao feito")