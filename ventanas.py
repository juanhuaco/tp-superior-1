import tkinter as tk
from PIL import ImageTk,Image  

def crearVentana1(ventana):

    ventana1 = tk.Toplevel(ventana)
    ventana1.geometry("1200x900")

    #Titulo
    titulo = tk.Label(ventana1, text="Ejercicio1")
    titulo.config(font=("Verdana", 24))
    titulo.pack()

    #Texto Principal
    parrafo = tk.Label(ventana1, text="Explicacion magistral")
    parrafo.config(font=("Verdana", 16))
    parrafo.pack()

    #Img       
    img = ImageTk.PhotoImage(Image.open("./imagenes/ej1pic.png").resize((650,300)))

    myLabel = tk.Label(ventana1, image=img)
    myLabel.pack()

    ventana1.mainloop()

def crearVentana2(ventana):
    ventana1 = tk.Toplevel(ventana)
    ventana1.geometry("1200x900")

    #Titulo
    titulo = tk.Label(ventana1, text="Ejercicio1")
    titulo.config(font=("Verdana", 24))
    titulo.pack()

    #Texto Principal
    parrafo = tk.Label(ventana1, text="Explicacion magistral")
    parrafo.config(font=("Verdana", 16))
    parrafo.pack()

    #Img       
    img = ImageTk.PhotoImage(Image.open("./imagenes/ej1pic.png").resize((600,400)))

    myLabel = tk.Label(ventana1, image=img)
    myLabel.pack()

    ventana1.mainloop()

def main():
    return

if __name__ == '__main__':
    main()