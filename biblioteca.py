import tkinter as tk
from tkinter import *
import csv
from tkinter import messagebox, ttk

#CLASE LIBRO
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