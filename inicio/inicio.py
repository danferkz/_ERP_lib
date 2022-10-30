from tkinter import*
import tkinter as tk

ventana= tk.Tk()
ventana.title("Login")
ventana.geometry("1916x1364+500+50")
ventana.resizable(width=False,height=False)
fondo=tk.PhotoImage(file="imagenes/INICIO.png")
fondo1 = tk.Label(ventana, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)
ventana.mainloop()