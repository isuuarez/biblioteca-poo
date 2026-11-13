
# Importamos la clase Socio
from modelo.socio import Socio


class SocioDAO:

    # Constructor
    def __init__(self, ruta_archivo):

        self.ruta_archivo = ruta_archivo
        self.socios = {}

    # Cargar los socios desde el archivo TXT
    def cargar(self):

        self.socios = {}

        with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:

            for linea in archivo:

                if not linea.strip():
                    continue

                datos = linea.strip().split(";")

                codigo = datos[0]
                nombre = datos[1]
                email = datos[2]
                codigo_libro = datos[3]

                if codigo_libro == "None":
                    codigo_libro = None

                socio = Socio(
                    codigo,
                    nombre,
                    email,
                    codigo_libro
                )

                self.socios[codigo] = socio

        return self.socios

    # Guardar los socios en el archivo TXT
    def guardar(self):

        with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:

            for socio in self.socios.values():

                codigo_libro = socio.codigo_libro

                if codigo_libro is None:
                    codigo_libro = "None"

                linea = (
                    f"{socio.codigo};{socio.nombre};"
                    f"{socio.email};{codigo_libro}\n"
                )

                archivo.write(linea)

    # Obtener todos los socios
    def obtener_todos(self):

        return self.socios

    # Buscar un socio por su codigo
    def obtener_por_codigo(self, codigo):

        return self.socios.get(codigo)

    # Anadir un socio nuevo
    def anadir(self, socio):

        if socio.codigo in self.socios:
            return False

        self.socios[socio.codigo] = socio

        return True

    # Actualizar un socio existente
    def actualizar(self, socio):

        if socio.codigo not in self.socios:
            return False

        self.socios[socio.codigo] = socio

        return True

    # Eliminar un socio
    def eliminar(self, codigo):

        if codigo not in self.socios:
            return False

        del self.socios[codigo]

        return True
