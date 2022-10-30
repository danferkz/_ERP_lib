from tkinter import*
import tkinter as tk

#colores
fondo_CONECTAR="#54556d"
fondo_ENTRADA="#ffffff"
#entradas




ventana= tk.Tk()
ventana.title("Login")
ventana.geometry("1916x1364+500+50")
ventana.resizable(width=False,height=False)
fondo=tk.PhotoImage(file="imagenes/nuevo fondo.png")
fondo1 = tk.Label(ventana, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)

usuario=tk.StringVar()
comtraseña=tk.StringVar()
#entradas
entrada=tk.Entry(ventana, text="USUARIO", width=32, bg=fondo_ENTRADA, font=("Inter", 50,), relief="flat")
entrada.place(x=434, y=650)
entrada2=tk.Entry(ventana, text="CONTRASEÑA", width=32, bg=fondo_ENTRADA, font=("Inter", 50,), relief="flat")
entrada2.place(x=434, y=850)
#Botones
boton1=tk.Button(ventana, text="CONECTAR", cursor="hand2", bg=fondo_CONECTAR, width=12, relief="flat", font=("Inter", 40,"bold"))
boton1.place(x=734, y=1185)
ventana.mainloop()