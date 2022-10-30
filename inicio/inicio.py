from ast import literal_eval
from tkinter import*
import tkinter as tk

#colores
fondo_CONECTAR="#54556d"
fondo_ENTRADA="#ffffff"
#entradas




ventana= tk.Tk()
ventana.title("INICIO")
ventana.geometry("1916x1364+500+50")
ventana.resizable(width=False,height=False)
fondo=tk.PhotoImage(file="imagenes/nuevo fondo.png")
fondo1 = tk.Label(ventana, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)

usuario=tk.StringVar()
comtraseña=tk.StringVar()
#entradas
def on_enter(a):
    entrada.delete(0,'end')
def on_leave(a):
    name=entrada.get()
    if name=="":
        entrada.insert(0,'USUARIO')
        
entrada=tk.Entry(ventana, text="USUARIO",fg="#7c7c7c", width=32, bg=fondo_ENTRADA, font=("Inter", 50,), relief="flat")
entrada.place(x=434, y=650)
entrada.insert(0,'USUARIO')
entrada.bind('<FocusIn>', on_enter)
entrada.bind('<FocusOut>', on_leave)

def on_enter(b):
    entrada2.delete(0,'end')
def on_leave(b):
    cont=entrada2.get()
    if cont=="":
        entrada2.insert(0,'CONTRASEÑA')

entrada2=tk.Entry(ventana, text="CONTRASEÑA",fg="#7c7c7c", width=32, bg=fondo_ENTRADA, font=("Calibri ", 50), relief="flat")
entrada2.place(x=434, y=850)
entrada2.insert(0,'CONTRASEÑA')
entrada2.bind('<FocusIn>', on_enter)
entrada2.bind('<FocusOut>', on_leave)
#Botones
boton1=tk.Button(ventana, text="CONECTAR",fg="#ffffff", cursor="hand2", bg=fondo_CONECTAR, width=12, relief="flat", font=("Inter", 40,"bold"))
boton1.place(x=734, y=1185)
ventana.mainloop()