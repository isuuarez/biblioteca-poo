
# Importamos los DAO
from dao.libro_dao import LibroDAO
from dao.socio_dao import SocioDAO

# Importamos las excepciones
from errores.excepciones import ErrorBiblioteca

# Importamos datetime para registrar la fecha y hora
from datetime import datetime


class Biblioteca:

    # Constructor
    def __init__(self, libro_dao, socio_dao, ruta_log="log.txt"):

        self.libro_dao = libro_dao
        self.socio_dao = socio_dao
        self.ruta_log = ruta_log

    # Cargar libros y socios
    def cargar_datos(self):

        self.libro_dao.cargar()
        self.socio_dao.cargar()

    # Guardar libros y socios
    def guardar_datos(self):

        self.libro_dao.guardar()
        self.socio_dao.guardar()

    # Registrar eventos en el archivo log.txt
    def registrar_evento(self, evento, detalles):

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.ruta_log, "a", encoding="utf-8") as archivo:

            archivo.write(f"[{fecha}][{evento}][{detalles}]\n")

    # Obtener todos los libros
    def obtener_todos_los_libros(self):

        return list(self.libro_dao.obtener_todos().values())

    # Obtener todos los socios
    def obtener_todos_los_socios(self):

        return list(self.socio_dao.obtener_todos().values())

    # Obtener solamente los libros disponibles
    def obtener_libros_disponibles(self):

        disponibles = []

        for libro in self.obtener_todos_los_libros():

            if libro.esta_disponible():
                disponibles.append(libro)

        return disponibles

    # Buscar libros por cualquier parte del titulo
    def buscar_libros(self, termino):

        termino = termino.strip().casefold()

        if not termino:
            return []

        resultados = []

        for libro in self.obtener_todos_los_libros():

            if termino in libro.titulo.casefold():
                resultados.append(libro)

        return resultados

    # Obtener socios que tienen libros prestados
    def obtener_socios_con_prestamos(self):

        resultados = []

        for socio in self.obtener_todos_los_socios():

            if socio.tiene_libro():

                libro = self.libro_dao.obtener_por_codigo(socio.codigo_libro)

                resultados.append((socio, libro))

        return resultados

    # Anadir un libro
    def anadir_libro(self, libro):

        return self.libro_dao.anadir(libro)

    # Anadir un socio
    def anadir_socio(self, socio):

        return self.socio_dao.anadir(socio)

    # Realizar un prestamo
    def prestar_libro(self, codigo_libro, codigo_socio):

        codigo_libro = codigo_libro.strip().upper()
        codigo_socio = codigo_socio.strip().upper()

        # Comprobamos que el libro existe
        libro = self.libro_dao.obtener_por_codigo(codigo_libro)

        if libro is None:
            raise ErrorBiblioteca(
                "LIBRO_NO_EXISTE",
                "El libro no existe."
            )

        # Comprobamos que el socio existe
        socio = self.socio_dao.obtener_por_codigo(codigo_socio)

        if socio is None:
            raise ErrorBiblioteca(
                "SOCIO_NO_EXISTE",
                "El socio no existe."
            )

        # Comprobamos que el libro esta disponible
        if not libro.esta_disponible():

            raise ErrorBiblioteca(
                "LIBRO_PRESTADO",
                "El libro ya esta prestado."
            )

        # Comprobamos que el socio no tenga otro libro
        if socio.tiene_libro():

            raise ErrorBiblioteca(
                "SOCIO_CON_LIBRO",
                "El socio ya tiene un libro prestado."
            )

        # Realizamos el prestamo
        libro.asignar_socio(codigo_socio)
        socio.asignar_libro(codigo_libro)

        # Actualizamos los objetos mediante los DAO
        self.libro_dao.actualizar(libro)
        self.socio_dao.actualizar(socio)

        # Registramos el prestamo
        self.registrar_evento(
            "PRESTAMO",
            f"Libro {codigo_libro} prestado al socio {codigo_socio}"
        )

        return libro

    # Realizar una devolucion
    def devolver_libro(self, codigo_socio):

        codigo_socio = codigo_socio.strip().upper()

        # Comprobamos que el socio existe
        socio = self.socio_dao.obtener_por_codigo(codigo_socio)

        if socio is None:

            raise ErrorBiblioteca(
                "SOCIO_NO_EXISTE",
                "El socio no existe."
            )

        # Comprobamos que tiene algun libro
        if not socio.tiene_libro():

            raise ErrorBiblioteca(
                "SIN_PRESTAMO",
                "El socio no tiene ningun libro prestado."
            )

        # Obtenemos el libro del socio
        codigo_libro = socio.codigo_libro

        libro = self.libro_dao.obtener_por_codigo(codigo_libro)

        if libro is None:

            raise ErrorBiblioteca(
                "LIBRO_NO_EXISTE",
                "No se encuentra el libro asociado al socio."
            )

        # Liberamos el libro y el socio
        libro.liberar()
        socio.liberar_libro()

        # Actualizamos los objetos mediante los DAO
        self.libro_dao.actualizar(libro)
        self.socio_dao.actualizar(socio)

        # Registramos la devolucion
        self.registrar_evento(
            "DEVOLUCION",
            f"Libro {codigo_libro} devuelto por el socio {codigo_socio}"
        )

        return libro
