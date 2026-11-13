
# Importamos las clases Libro y Socio
from modelo.libro import Libro
from modelo.socio import Socio
from errores.excepciones import ErrorBiblioteca
from datetime import datetime


# Rutas de los archivos
RUTA_LIBROS = "datos/libros.txt"
RUTA_SOCIOS = "datos/socios.txt"
RUTA_LOG = "log.txt"



# Funcion para cargar los libros desde el archivo TXT
def cargar_libros():

    libros = {}

    with open(RUTA_LIBROS, "r", encoding="utf-8") as archivo:

        for linea in archivo:

            datos = linea.strip().split(";")

            codigo = datos[0]
            titulo = datos[1]
            autor = datos[2]
            anio = int(datos[3])
            categoria = datos[4]
            codigo_socio = datos[5]

            # Convertimos el texto None en el valor None de Python
            if codigo_socio == "None":
                codigo_socio = None

            # Creamos el objeto Libro
            libro = Libro(codigo, titulo, autor, anio,
                          categoria, codigo_socio)

            # Guardamos el libro en el diccionario
            libros[codigo] = libro

    return libros


# Funcion para cargar los socios desde el archivo TXT
def cargar_socios():

    socios = {}

    with open(RUTA_SOCIOS, "r", encoding="utf-8") as archivo:

        for linea in archivo:

            datos = linea.strip().split(";")

            codigo = datos[0]
            nombre = datos[1]
            email = datos[2]
            codigo_libro = datos[3]

            # Convertimos el texto None en el valor None de Python
            if codigo_libro == "None":
                codigo_libro = None

            # Creamos el objeto Socio
            socio = Socio(codigo, nombre, email, codigo_libro)

            # Guardamos el socio en el diccionario
            socios[codigo] = socio

    return socios


# Funcion para guardar los libros en el archivo TXT
def guardar_libros(libros):

    with open(RUTA_LIBROS, "w", encoding="utf-8") as archivo:

        for libro in libros.values():

            codigo_socio = libro.codigo_socio

            # Si el libro esta disponible, escribimos None
            if codigo_socio is None:
                codigo_socio = "None"

            linea = (f"{libro.codigo};{libro.titulo};{libro.autor};"
                     f"{libro.anio};{libro.categoria};{codigo_socio}\n")

            archivo.write(linea)


# Funcion para guardar los socios en el archivo TXT
def guardar_socios(socios):

    with open(RUTA_SOCIOS, "w", encoding="utf-8") as archivo:

        for socio in socios.values():

            codigo_libro = socio.codigo_libro

            # Si el socio no tiene libro, escribimos None
            if codigo_libro is None:
                codigo_libro = "None"

            linea = (f"{socio.codigo};{socio.nombre};"
                     f"{socio.email};{codigo_libro}\n")

            archivo.write(linea)



# Funcion para registrar los eventos de la biblioteca
def registrar_evento(evento, detalles):

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(RUTA_LOG, "a", encoding="utf-8") as archivo:

        archivo.write(f"[{fecha}][{evento}][{detalles}]\n")


# Funcion para prestar un libro a un socio
def prestar_libro(libros, socios):

    try:

        # Pedimos los codigos
        print("\nIntroduce el codigo del libro:")
        codigo_libro = input("> ").strip().upper()

        print("Introduce el codigo del socio:")
        codigo_socio = input("> ").strip().upper()
        
        # Comprobamos que el libro existe
        if codigo_libro not in libros:
            raise ErrorBiblioteca("LIBRO_NO_EXISTE", "El libro no existe.")

        # Comprobamos que el socio existe
        if codigo_socio not in socios:
            raise ErrorBiblioteca("SOCIO_NO_EXISTE", "El socio no existe.")

        # Obtenemos los objetos
        libro = libros[codigo_libro]
        socio = socios[codigo_socio]

        # Comprobamos que el libro esta disponible
        if not libro.esta_disponible():
            raise ErrorBiblioteca("LIBRO_PRESTADO", "El libro ya esta prestado.")

        # Comprobamos que el socio no tiene otro libro
        if socio.tiene_libro():
            raise ErrorBiblioteca("SOCIO_CON_LIBRO", "El socio ya tiene un libro.")

        # Realizamos el prestamo
        libro.asignar_socio(codigo_socio)
        socio.asignar_libro(codigo_libro)

        # Registramos el evento
        registrar_evento(
            "PRESTAMO",
            f"Libro {codigo_libro} prestado al socio {codigo_socio}"
        )

        print("Prestamo realizado correctamente.")

    except ErrorBiblioteca as error:

        print("ERROR:", error.mensaje)
        print("Codigo:", error.codigo)



# Funcion para devolver el libro de un socio
def devolver_libro(libros, socios):

    try:

        # Pedimos el codigo del socio
        codigo_socio = input("Introduce el codigo del socio: ").strip().upper()

        # Comprobamos que el socio existe
        if codigo_socio not in socios:
            raise ErrorBiblioteca("SOCIO_NO_EXISTE", "El socio no existe.")

        # Obtenemos el socio
        socio = socios[codigo_socio]

        # Comprobamos que tiene algun libro
        if not socio.tiene_libro():
            raise ErrorBiblioteca("SIN_PRESTAMO", "El socio no tiene ningun libro.")

        # Obtenemos el codigo del libro
        codigo_libro = socio.codigo_libro

        # Comprobamos que el libro existe
        if codigo_libro not in libros:
            raise ErrorBiblioteca("LIBRO_NO_EXISTE", "El libro asociado no existe.")

        # Obtenemos el libro
        libro = libros[codigo_libro]

        # Liberamos el libro y el socio
        libro.liberar()
        socio.liberar_libro()

        # Registramos el evento
        registrar_evento(
            "DEVOLUCION",
            f"Libro {codigo_libro} devuelto por el socio {codigo_socio}"
        )

        print("Devolucion realizada correctamente.")

    except ErrorBiblioteca as error:

        print("ERROR:", error.mensaje)
        print("Codigo:", error.codigo)

# PRUEBAS TEMPORALES DE LA FASE 5

if __name__ == "__main__":

    # Cargamos los datos
    libros = cargar_libros()
    socios = cargar_socios()

    print("Biblioteca cargada correctamente.")
    print("Libros:", len(libros))
    print("Socios:", len(socios))

    print("\n----- REALIZAR PRESTAMO -----")
    prestar_libro(libros, socios)

    # Guardamos los cambios del prestamo
    guardar_libros(libros)
    guardar_socios(socios)

    print("\n----- REALIZAR DEVOLUCION -----")
    devolver_libro(libros, socios)

    # Guardamos los cambios de la devolucion
    guardar_libros(libros)
    guardar_socios(socios)

    print("\nPruebas finalizadas.")
