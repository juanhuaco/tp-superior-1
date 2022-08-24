import tkinter as tk
import tp

def main():
    ventana = tk.Tk()
    ventana.geometry("200x160")
    ventana.title("Matematica Superior TP1")
    
    label = tk.Label(ventana, text = "Matematica Superior TP1", height=2)
    label.pack()

    ejercicio1Btn = tk.Button(ventana, text="Ejercicio 1", command=tp.ejercicio1)
    ejercicio1Btn.pack()

    ejercicio2Btn = tk.Button(ventana, text="Ejercicio 2", command=tp.ejercicio2)
    ejercicio2Btn.pack()

    ejercicio3Btn = tk.Button(ventana, text="Ejercicio 3", command=tp.ejercicio3)
    ejercicio3Btn.pack()

    ejercicio4Btn = tk.Button(ventana, text="Ejercicio 4", command=tp.ejercicio4)
    ejercicio4Btn.pack()


    ventana.mainloop()

if __name__ == '__main__':
    main()