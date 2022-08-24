from functools import reduce
from scipy.fft import fft
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

#definir datos
f = open("calamar_pda.txt")

NoInteresa1 =  f.readline()
DatosTiempo = f.readline()
NoInteresa2 = f.readline()
DatosPotencialMembrana = f.readline()

PotencialMembrana = list(map(float, (DatosPotencialMembrana.split(","))))
Tiempo =list(map(float, (DatosTiempo.split(","))))


N = len(PotencialMembrana)
T = 1 / N # 0.1/N

yf = fft(PotencialMembrana)
xf = np.linspace(0, 1/(2*T), N//2)

#EJERCICIO1
def ejercicio1():

    fig, [ax1Ej1, ax2Ej1] = plt.subplots(nrows=1, ncols=2)
    fig.set_size_inches(13, 6)

    ax1Ej1.plot(xf, 2/N * np.abs(PotencialMembrana[:N//2]), 1)
    plt.subplot(1,2,1)
    plt.title("Ejercicio 1 - Sin Transformar")
    plt.ylabel("PotencialMembrana [mV]")
    plt.xlabel("Tiempo [ms]")

    ax2Ej1.plot(xf, 2/N * np.abs(yf[:N//2]), 2)

    plt.subplot(1,2,2)
    plt.title("Ejercicio 1 - Transformado")
    plt.ylabel("Amplitud []")
    plt.xlabel("Frecuencia []")

    plt.show()

    return



### EJERCICIO2
def ejercicio2():
    def funcion_escalon(t):
        if(t >= 0):
            return 1
        else:
            return 0

    def lomo( a, time_step, Ti, Tf):
        if(a < 0):
            a = -a

        T = np.arange(Ti, Tf, time_step)
        Y = []

        for i in T:
            value = (funcion_escalon(i+a) - funcion_escalon(i-a)) / (2*a)
            Y.append(value)

        return (T, Y)

    a = 15
    time_step = 1

    T, Y = lomo(a,time_step, -a, a + 1)

    filtered = signal.convolve(PotencialMembrana, Y)

    plt.plot(filtered)
    plt.title("Ejercicio 2 - Funcion Filtrada")
    plt.show()

    plt.stem(T,Y)
    plt.title("Ejercicio 2 - Funcion Lomo")
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

    plt.figure(1)
    plt.title('Filtro en la frecuencia')
    plt.plot(cant_puntos, escalon, '.-')
    plt.grid()
    plt.show()


    #Antitransformada
    antitransformada_escalon = np.fft.ifft(escalon)

    plt.figure(2)
    plt.title('Antitransformada del filtro (sinc)')
    plt.plot(cant_puntos, antitransformada_escalon)
    plt.grid()
    plt.xlim([0,1000])
    plt.show()

    #Aplicar el filtro a la transformada del Potencial
    #Para aplicarlo hicimos una convolucion, multiplicamos en frecuencia y antitransformamos
    filtrada = escalon * yf
    plt.figure(3)
    plt.title('Transformada del potencial filtrada')
    plt.plot(cant_puntos, filtrada)
    plt.grid()
    #plt.show()

    antitransformada_filtrada = np.fft.ifft(filtrada)
    plt.figure(4)
    plt.title('Antitransformada de filtrada')
    plt.plot(cant_puntos, antitransformada_filtrada)
    plt.grid()
    #plt.show()

def ejercicio4():
    print("ainda nao feito")