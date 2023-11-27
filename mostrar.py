import subprocess
import tkinter as tk
import pandas as pd
from pandastable import Table

def regresar():
    window.destroy()
    subprocess.Popen('python principal.py', shell=True)
    
# Crea una ventana de tkinter
window = tk.Tk()
window.iconbitmap("icono.ico")
# Establece el tamaño de la ventana a 700x550
window.geometry("700x550")
window.title("Mostrar")

# Lee los datos del archivo CSV usando pandas
df = pd.read_csv('biblioteca.csv')

# Crea un Frame en la ventana de tkinter para la tabla
frame = tk.Frame(window)
frame.pack(fill='both', expand=True)

# Usa pandastable para crear una tabla y añadirla al Frame
pt = Table(frame, dataframe=df)

# Ajusta el ancho de las columnas para que se ajusten al contenido
pt.autoResizeColumns()
df = df.sort_values('Titulo')
pt.show()

# Crea un nuevo Frame para el botón
frame_boton = tk.Frame(window)
frame_boton.pack(fill='x', expand=False)

# Crea un botón de regresar dentro del nuevo Frame
boton_regresar = tk.Button(frame_boton, text="Regresar", command=regresar)
boton_regresar.pack(side='right')

# Inicia el bucle principal de tkinter

window.mainloop()
