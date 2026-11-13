
# Importamos las clases Libro y Socio
from modelo.libro import Libro
from modelo.socio import Socio


# Rutas de los archivos
RUTA_LIBROS = "datos/libros.txt"
RUTA_SOCIOS = "datos/socios.txt"


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


# PRUEBA TEMPORAL DE LA FASE 4

if __name__ == "__main__":

    # Cargamos los libros y los socios
    libros = cargar_libros()
    socios = cargar_socios()

    # Mostramos la cantidad de registros cargados
    print("INFORMACION CARGADA CORRECTAMENTE")
    print("Libros cargados:", len(libros))
    print("Socios cargados:", len(socios))

    # Mostramos un libro y un socio de ejemplo
    print("\nPRIMER LIBRO:")
    libro = libros["L001"]
    print(libro.codigo, libro.titulo, libro.autor)

    print("\nPRIMER SOCIO:")
    socio = socios["S001"]
    print(socio.codigo, socio.nombre, socio.email)

    # Guardamos los datos en los archivos TXT
    guardar_libros(libros)
    guardar_socios(socios)

    print("\nDatos guardados correctamente.")

    # Volvemos a cargar los archivos para comprobarlos
    libros = cargar_libros()
    socios = cargar_socios()

    print("\nCOMPROBACION FINAL")
    print("Libros despues de guardar:", len(libros))
    print("Socios despues de guardar:", len(socios))
