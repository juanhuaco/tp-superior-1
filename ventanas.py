from os import X_OK
import tkinter as tk
from PIL import ImageTk,Image  
import tp

def crearVentana2(ventana):
    ventana1 = tk.Toplevel(ventana)
    ventana1.geometry("200x160")

    #a
    aLabel = tk.Label(ventana1, text="a:")
    aLabel.config(font=("Verdana", 16))
    aLabel.pack()

    aTxt = tk.Text(ventana1,
                   height = 1,
                   width = 20)
    aTxt.pack()

    #plot

    plotBtn = tk.Button(ventana1, text="Plot", command= lambda : tp.ejercicio2(int(aTxt.get(1.0, "end-1c"))))
    plotBtn.pack()

    ventana1.mainloop()

def crearVentana3(ventana):
    ventana1 = tk.Toplevel(ventana)
    ventana1.geometry("200x160")

    #b1
    b1Label = tk.Label(ventana1, text="b de func1:")
    b1Label.config(font=("Verdana", 16))
    b1Label.pack()

    b1Txt = tk.Text(ventana1,
                   height = 1,
                   width = 20)
    b1Txt.pack()

    #b2
    b2Label= tk.Label(ventana1, text="b de func2:")
    b2Label.config(font=("Verdana", 16))
    b2Label.pack()
    
    b2Txt = tk.Text(ventana1,
                   height = 1,
                   width = 20)
    b2Txt.pack()
    
    #plot

    plotBtn = tk.Button(ventana1, text="Plot", command= lambda : tp.ejercicio3(float(b1Txt.get(1.0, "end-1c")), float(b2Txt.get(1.0, "end-1c"))))
    plotBtn.pack()

    ventana1.mainloop()

def crearVentana4(ventana):

    ventana1 = tk.Toplevel(ventana)
    ventana1.geometry("200x160")

    #r
    rLabel = tk.Label(ventana1, text="R:")
    rLabel.config(font=("Verdana", 16))
    rLabel.pack()

    rTxt = tk.Text(ventana1,
                   height = 1,
                   width = 20)
    rTxt.pack()

    #c
    cLabel= tk.Label(ventana1, text="C:")
    cLabel.config(font=("Verdana", 16))
    cLabel.pack()
    
    cTxt = tk.Text(ventana1,
                   height = 1,
                   width = 20)
    cTxt.pack()
    
    #plot

    plotBtn = tk.Button(ventana1, text="Plot", command= lambda : tp.ejercicio4(rTxt.get(1.0, "end-1c"), cTxt.get(1.0, "end-1c")))
    plotBtn.pack()

    ventana1.mainloop()


def main():
    return

if __name__ == '__main__':
    main()