
# Importamos la clase Libro
from modelo.libro import Libro


class LibroDAO:

    # Constructor
    def __init__(self, ruta_archivo):

        self.ruta_archivo = ruta_archivo
        self.libros = {}

    # Cargar los libros desde el archivo TXT
    def cargar(self):

        self.libros = {}

        with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:

            for linea in archivo:

                datos = linea.strip().split(";")

                if not linea.strip():
                    continue

                codigo = datos[0]
                titulo = datos[1]
                autor = datos[2]
                anio = int(datos[3])
                categoria = datos[4]
                codigo_socio = datos[5]

                if codigo_socio == "None":
                    codigo_socio = None

                libro = Libro(
                    codigo,
                    titulo,
                    autor,
                    anio,
                    categoria,
                    codigo_socio
                )

                self.libros[codigo] = libro

        return self.libros

    # Guardar los libros en el archivo TXT
    def guardar(self):

        with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:

            for libro in self.libros.values():

                codigo_socio = libro.codigo_socio

                if codigo_socio is None:
                    codigo_socio = "None"

                linea = (
                    f"{libro.codigo};{libro.titulo};{libro.autor};"
                    f"{libro.anio};{libro.categoria};{codigo_socio}\n"
                )

                archivo.write(linea)

    # Obtener todos los libros
    def obtener_todos(self):

        return self.libros

    # Buscar un libro por su codigo
    def obtener_por_codigo(self, codigo):

        return self.libros.get(codigo)

    # Anadir un libro nuevo
    def anadir(self, libro):

        if libro.codigo in self.libros:
            return False

        self.libros[libro.codigo] = libro

        return True

    # Actualizar un libro existente
    def actualizar(self, libro):

        if libro.codigo not in self.libros:
            return False

        self.libros[libro.codigo] = libro

        return True

    # Eliminar un libro
    def eliminar(self, codigo):

        if codigo not in self.libros:
            return False

        del self.libros[codigo]

        return True
