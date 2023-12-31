
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox,ttk
import subprocess
import tkinter as tk
import csv



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame3")
fuente=("Righteous Regular", 15)

class Libro:
    def __init__(self, titulo, autor, genero, anio_publicacion, estado):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.anio_publicacion = anio_publicacion
        self.estado = estado

# Definición de la clase Biblioteca
class Biblioteca: 
    def __init__(self):
        self.libros = []
        self.cargar_csv()

    def agregar_libro(self, libro):
        # Verifica si el libro ya existe en la biblioteca
        if any(libro.titulo.lower() == existing_libro.titulo.lower() for existing_libro in self.libros):
            messagebox.showinfo("Libro Existente", f"El libro '{libro.titulo}' ya existe en la biblioteca.")
        else:
            self.libros.append(libro)
            self.guardar_en_csv(libro)
            print("\nLibro registrado con éxito.")
            

    def cargar_csv(self):
        try:
            with open('biblioteca.csv', mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 5:
                        libro = Libro(row[0], row[1], row[2], row[3], row[4])
                        self.libros.append(libro)
        except FileNotFoundError:
            pass

    def guardar_en_csv(self, libro):
        with open("biblioteca.csv", mode="a", newline='', encoding='utf-8') as file:
            escribir = csv.writer(file)
            escribir.writerow([libro.titulo, libro.autor, libro.genero, libro.anio_publicacion, libro.estado])

    def reservar_libro(self, titulo_libro):
        for libro in self.libros:
            if libro.titulo.lower() == titulo_libro.lower():
                if libro.estado == "Disponible":
                    libro.estado = "Reservado"
                    self.actualizar_csv()
                    print(f"Libro '{libro.titulo}' reservado con éxito.")
                    return
        print(f"El libro '{titulo_libro}' no se encuentra disponible para reserva.")

    def actualizar_csv(self):
        with open("biblioteca.csv", mode="w", newline='', encoding='utf-8') as file:
            escribir = csv.writer(file)
            for libro in self.libros:
                escribir.writerow([libro.titulo, libro.autor, libro.genero, libro.anio_publicacion, libro.estado])

    def buscar_libros(self, criterio_busqueda):
        libros_encontrados = []
        for libro in self.libros:
            if criterio_busqueda.lower() in libro.titulo.lower() or criterio_busqueda.lower() in libro.autor.lower() or criterio_busqueda.lower() in libro.genero.lower():
                libros_encontrados.append(libro)

        if not libros_encontrados:
            messagebox.showinfo("Búsqueda sin Resultados", "No se encontraron libros que coincidan con el criterio de búsqueda.")
        
        else:

            ventana_resultados = tk.Toplevel()
            ventana_resultados.title("Resultados de Búsqueda")

        for libro in libros_encontrados:
            estado = "Disponible" if libro.estado == "Disponible" else "Reservado"

            etiqueta_titulo = tk.Label(ventana_resultados, text=f"Título: {libro.titulo}")
            etiqueta_titulo.pack()

            etiqueta_autor = tk.Label(ventana_resultados, text=f"Autor: {libro.autor}")
            etiqueta_autor.pack()

            etiqueta_genero = tk.Label(ventana_resultados, text=f"Género: {libro.genero}")
            etiqueta_genero.pack()

            etiqueta_anio = tk.Label(ventana_resultados, text=f"Año de Publicación: {libro.anio_publicacion}")
            etiqueta_anio.pack()

            etiqueta_estado = tk.Label(ventana_resultados, text=f"Estado: {estado}")
            etiqueta_estado.pack()

            separador = ttk.Separator(ventana_resultados, orient="horizontal")
            separador.pack(fill="x", padx=10, pady=5) 

    def cancelar_libro(self, titulo_libro):
        for libro in self.libros:
            if libro.titulo.lower() == titulo_libro.lower():
                if libro.estado == "Reservado":
                    libro.estado = "Disponible"
                    self.actualizar_csv()
                    print(f"Libro '{libro.titulo}' Cancelado con éxito.")
                    return
        print(f"El libro '{titulo_libro}' esta disponible.")

    
    def eliminar_libro(self, titulo_libro):

        libro_encontrado = None
        for libro in self.libros:
            if libro.titulo.lower() == titulo_libro.lower():
                opc = messagebox.askquestion("Eliminar Libro", "¿Estás seguro de querer eliminar este libro?", icon='warning')
                if opc == "yes":
                    libro_encontrado = libro
                    break
                elif opc == "no":
                    messagebox.showinfo("Eliminación Cancelada", "No se modificó ningún registro.")
                    return

        if libro_encontrado is not None:
            self.libros.remove(libro_encontrado)
            messagebox.showinfo("Libro Eliminado", "El libro ha sido eliminado con éxito.")
            self.actualizar_csv()

    def modificar_libro(self, titulo_libro):
        libro_encontrado = None
        for libro in self.libros:
            if libro.titulo.lower() == titulo_libro.lower():
                libro_encontrado = libro
                break  # Sal del bucle, ya que hemos encontrado el libro

        if libro_encontrado is not None:
            ventana_modificar = tk.Toplevel()
            ventana_modificar.title("Modificar Libro")

            etiqueta_opciones = tk.Label(ventana_modificar, text="¿Qué deseas modificar?")
            etiqueta_opciones.pack()

            opcion_var = tk.StringVar()
            opciones = ["Título", "Autor", "Género", "Año de Publicación", "Estado"]
            opcion_var.set(opciones[0])
            menu_opciones = ttk.Combobox(ventana_modificar, textvariable=opcion_var, values=opciones)
            menu_opciones.pack()

            nuevo_valor = tk.StringVar()
            entrada_nuevo_valor = tk.Entry(ventana_modificar, textvariable=nuevo_valor)
            entrada_nuevo_valor.pack()

            def aplicar_modificacion():
                opcion_seleccionada = opcion_var.get()
                valor_modificado = nuevo_valor.get()
                if opcion_seleccionada == "Título":
                    libro_encontrado.titulo = valor_modificado
                elif opcion_seleccionada == "Autor":
                    libro_encontrado.autor = valor_modificado
                elif opcion_seleccionada == "Género":
                    libro_encontrado.genero = valor_modificado
                elif opcion_seleccionada == "Año de Publicación":
                    libro_encontrado.anio_publicacion = valor_modificado
                elif opcion_seleccionada == "Estado":
                    libro_encontrado.estado = valor_modificado

                ventana_modificar.destroy()  # Cierra la ventana de modificación

                # Ahora, actualiza el archivo CSV con los cambios
                self.actualizar_csv()
                messagebox.showinfo("Modificación Exitosa", "El libro ha sido modificado con éxito.")

            boton_aplicar = tk.Button(ventana_modificar, text="Aplicar Modificación", command=aplicar_modificacion)
            boton_aplicar.pack()

            ventana_modificar.mainloop()


biblioteca = Biblioteca()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def regresar():
    window.destroy()
    subprocess.Popen('python principal.py', shell=True)

def escribir_datos():

      
    # Obtén los datos ingresados por el usuario
    titulo = entry_1.get()
    autor = entry_2.get()
    genero = entry_3.get()
    anio_publicacion = entry_4.get()
    estado = "Disponible"

    # Crea una instancia de la clase Libro
    nuevo_libro = Libro(titulo, autor, genero, anio_publicacion, estado)

    # Agrega el libro a la biblioteca y escribe los datos en el archivo CSV
    biblioteca.agregar_libro(nuevo_libro)

    biblioteca.actualizar_csv()

    # Limpia los campos de entrada después de escribir los datos
    entry_1.delete(0, 'end')
    entry_2.delete(0, 'end')
    entry_3.delete(0, 'end')
    entry_4.delete(0, 'end')



window = Tk()

window.geometry("700x550")
window.configure(bg = "#ECECC4")


canvas = Canvas(
    window,
    bg = "#ECECC4",
    height = 550,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    700.0,
    87.0,
    fill="#F1C40F",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=escribir_datos,
    relief="flat"
)
button_1.place(
    x=248.0,
    y=462.0,
    width=202.0,
    height=58.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=regresar,
    relief="flat"
)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    445.0,
    159.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F2DD88",
    fg="#947A1F",
    highlightthickness=0,
    font=fuente,
    
)
entry_1.place(
    x=302.0,
    y=133.0,
    width=286.0,
    height=50.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    445.0,
    239.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F2DD88",
    fg="#947A1F",
    highlightthickness=0,
    font=fuente
    
)
entry_2.place(
    x=302.0,
    y=213.0,
    width=286.0,
    height=50.0
)

canvas.create_text(
    214.0,
    6.0,
    anchor="nw",
    text="Agregar",
    fill="#F5F5DC",
    font=("Righteous Regular", 70 * -1)
)

canvas.create_text(
    121.0,
    141.0,
    anchor="nw",
    text="Titulo:",
    fill="#E67E22",
    font=("Righteous Regular", 30 * -1)
)

canvas.create_text(
    122.0,
    390.0,
    anchor="nw",
    text="Año:",
    fill="#E67E22",
    font=("Righteous Regular", 30 * -1)
)

canvas.create_text(
    111.0,
    306.0,
    anchor="nw",
    text="Genero:",
    fill="#E67E22",
    font=("Righteous Regular", 30 * -1)
)

canvas.create_text(
    121.0,
    221.0,
    anchor="nw",
    text="Autor:",
    fill="#E67E22",
    font=("Righteous Regular", 30 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    445.0,
    324.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#F2DD88",
    fg="#947A1F",
    highlightthickness=0,
    font=fuente
)
entry_3.place(
    x=302.0,
    y=298.0,
    width=286.0,
    height=50.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    445.0,
    408.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#F2DD88",
    fg="#947A1F",
    highlightthickness=0,
    font=fuente
)
entry_4.place(
    x=302.0,
    y=382.0,
    width=286.0,
    height=50.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    255.0,
    239.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    255.0,
    160.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    255.0,
    324.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    255.0,
    408.0,
    image=image_image_4
)


button_2.place(
    x=16.0,
    y=4.0,
    width=72.0,
    height=79.0
)



window.resizable(False, False)
window.mainloop()
