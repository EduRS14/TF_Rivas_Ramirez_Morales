from tkinter import *
import os
from PIL import ImageTk, Image

raiz = Tk()

raiz.title("Interfaz gráfica")
raiz.resizable(False, False)
raiz.iconbitmap("grafos_logo.ico")
raiz.geometry("800x600")
raiz.config(bg = "sky blue")

frame1 = Frame(raiz)

#frame1.pack(side = "left", anchor = "n")
#frame1.pack(fill="both", expand="True")
frame1.config(bg = "white")
frame1.config(width = "500", height = "400")
frame1.config(bd =  5)  
frame1.config(relief = "ridge")
frame1.config(cursor="hand2")
frame1.place(x = 150, y = 100)

label1 = Label(raiz, text = "Programa (Prueba de GUI)", fg = "black", font = ("Comic Sans MS", 20), bg = "sky blue")
label1.place(x = 10, y = 20)
imagen = ImageTk.PhotoImage(Image.open("grafos_logo.png").resize((100,100)))
Label(frame1, image = imagen).place(x = 200, y = 150)

raiz.mainloop() 