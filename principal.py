
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import subprocess

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def mostrar():
    window.destroy()
    subprocess.Popen('python mostrar.py', shell=True)

def agregar():
    window.destroy()
    subprocess.Popen('python agregar.py', shell=True)
    
def buscar():
    window.destroy()
    subprocess.Popen('python buscar.py', shell=True)

def reservar():
    window.destroy()
    subprocess.Popen('python reservar.py', shell=True)

window = Tk()
window.title("Bienvenido!")
window.iconbitmap("icono.ico")
window.geometry("700x550")
window.configure(bg = "#EBEBC3")


canvas = Canvas(
    window,
    bg = "#EBEBC3",
    height = 550,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    438.0,
    294.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    441.0,
    434.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=reservar,
    relief="flat",
    cursor="hand2"
)
button_1.place(
    x=506.0,
    y=279.0,
    width=150.0,
    height=40.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Editar btn"),
    relief="flat",
    cursor="hand2"
)
button_2.place(
    x=506.0,
    y=409.0,
    width=150.0,
    height=40.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=mostrar,
    relief="flat",
    cursor="hand2"
)
button_3.place(
    x=506.0,
    y=161.0,
    width=150.0,
    height=40.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    438.0,
    171.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    95.0,
    434.0,
    image=image_image_4
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Eliminar boton"),
    relief="flat",
    cursor="hand2"
)
button_4.place(
    x=168.0,
    y=408.0,
    width=150.0,
    height=40.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=buscar,
    relief="flat",
    cursor="hand2"
)
button_5.place(
    x=168.0,
    y=162.0,
    width=150.0,
    height=40.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=agregar,
    relief="flat",
    cursor="hand2"
)
button_6.place(
    x=168.0,
    y=280.0,
    width=150.0,
    height=40.0
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    95.0,
    294.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    95.0,
    171.0,
    image=image_image_6
)

canvas.create_rectangle(
    0.0,
    0.0,
    700.0,
    87.0,
    fill="#F1C40F",
    outline="")

canvas.create_text(
    188.0,
    2.0,
    anchor="nw",
    text="Biblioteca",
    fill="#F5F5DC",
    font=("Righteous Regular", 70 * -1)
)
window.resizable(False, False)
window.mainloop()
