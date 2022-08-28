import tkinter as tk
import ventanas as v
import tp

def main():
    ventana = tk.Tk()
    ventana.geometry("200x160")
    ventana.title("Matematica Superior TP1")
    
    label = tk.Label(ventana, text = "Matematica Superior TP1", height=2)
    label.pack()

    ejercicio1Btn = tk.Button(ventana, text="Ejercicio 1", command= tp.ejercicio1)
    ejercicio1Btn.pack()

    ejercicio2Btn = tk.Button(ventana, text="Ejercicio 2", command= lambda: v.crearVentana2(ventana))
    ejercicio2Btn.pack()

    ejercicio3Btn = tk.Button(ventana, text="Ejercicio 3", command= lambda: v.crearVentana3(ventana))
    ejercicio3Btn.pack()

    ejercicio4Btn = tk.Button(ventana, text="Ejercicio 4", command= lambda: v.crearVentana4(ventana))
    ejercicio4Btn.pack()

    exitBtn = tk.Button(ventana, text="Exit", command=ventana.quit)
    exitBtn.pack()

    ventana.mainloop()

if __name__ == '__main__':
    main()