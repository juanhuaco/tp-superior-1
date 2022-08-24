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
T = 1 / N # 0.1/N

PMfft = fft(PotencialMembrana)
xf = np.linspace(0, 100 * N , N)

#EJERCICIO1
def ejercicio1():

    fig, [ax1Ej1, ax2Ej1] = plt.subplots(nrows=1, ncols=2)
    fig.set_size_inches(13, 6)


    ax1Ej1.plot(xf, PotencialMembrana, 1)
    plt.subplot(1,2,1)
    plt.title("Ejercicio 1 - Sin Transformar")
    plt.ylabel("PotencialMembrana [mV]")
    plt.xlabel("Tiempo [ms]")
    plt.grid()
 
    ax2Ej1.plot(xf, 2/N * np.abs(PMfft), 2)
    plt.subplot(1,2,2)
    plt.title("Ejercicio 1 - Transformado")
    plt.ylabel("Amplitud []")
    plt.xlabel("Frecuencia []")
    plt.grid()

    plt.savefig("./imagenes/ej1pic.png")

    return



### EJERCICIO2
def ejercicio2():
    def funcion_escalon(t):
        if(t >= 0):
            return 1
        else:
            return 0

    def getLoma(a, timeStep):
        a = abs(a)

        loma = lambda p:  (funcion_escalon(p+a) - funcion_escalon(p-a)) / (2*a)

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
    #Construccion del escalon en la frecuencia 3


    escalon = []
    N = len(PotencialMembrana) #1001 

    cant_puntos = np.linspace(0, 10000, N)

    b = 1000

    #Con este for armamos el filtro ya espejado y con los 1001 puntos
    for i in cant_puntos:
        if ((i >= 0 and i < b) or (i >= (10000-b))):
            escalon.append(1)
        elif (i == b):
            escalon.append(1/2)
        else:
            escalon.append(0)

    #plotting
    #plotting
    fig, ax = plt.subplots(nrows=2, ncols=2)
    fig.set_size_inches(12, 8)

    #plt.figure(1)
    plt.title('Filtro en la frecuencia')
    plt.subplot(2,2,1)
    ax[0,0].plot(cant_puntos, escalon, '.-')
    plt.grid()


    #Antitransformada
    antitransformada_escalon = np.fft.ifft(escalon)

    #plt.figure(2)
    plt.subplot(2,2,2)
    plt.title('Antitransformada del filtro (sinc)')
    ax[1,0].plot(cant_puntos, antitransformada_escalon)
    plt.grid()
    plt.xlim([0,1000])

    #Aplicar el filtro a la transformada del Potencial
    #Para aplicarlo hicimos una convolucion, multiplicamos en frecuencia y antitransformamos
    filtrada = escalon * yf
    #plt.figure(3)
    plt.subplot(2,2,3)
    plt.title('Transformada del potencial filtrada')
    ax[0,1].plot(cant_puntos, filtrada)
    plt.grid()

    antitransformada_filtrada = np.fft.ifft(filtrada)
    #plt.figure(4)
    plt.subplot(2,2,4)
    plt.title('Antitransformada de filtrada')
    ax[1,1].plot(cant_puntos, antitransformada_filtrada)
    plt.grid()
    plt.show()

def ejercicio4():
    print("ainda nao feito")