
# Importamos las clases Libro y Socio
from modelo.libro import Libro
from modelo.socio import Socio
from errores.excepciones import ErrorBiblioteca
from datetime import datetime


# Rutas de los archivos
RUTA_LIBROS = "datos/libros.txt"
RUTA_SOCIOS = "datos/socios.txt"
RUTA_LOG = "log.txt"


# Funcion para mostrar los datos de un libro
def mostrar_datos_libro(libro):

    if libro.esta_disponible():
        estado = "Disponible"
    else:
        estado = "Prestado"

    print(
        f"{libro.codigo} | {libro.titulo} | "
        f"{libro.autor} | {libro.anio} | "
        f"{libro.categoria} | {estado}"
    )


# Funcion para mostrar todos los libros
def mostrar_libros(libros):

    print("\n--------------- TODOS LOS LIBROS ---------------")
    print("CODIGO | TITULO | AUTOR | ANIO | CATEGORIA | ESTADO")

    for libro in libros.values():
        mostrar_datos_libro(libro)


# Funcion para mostrar solamente los libros disponibles
def mostrar_disponibles(libros):

    print("\n--------------- LIBROS DISPONIBLES ---------------")

    encontrados = False

    for libro in libros.values():

        if libro.esta_disponible():
            mostrar_datos_libro(libro)
            encontrados = True

    if not encontrados:
        print("No hay libros disponibles.")


# Funcion para buscar un libro por su titulo
def buscar_libro(libros):

    termino = input("\nIntroduce el titulo o una parte del titulo: ").strip().casefold()

    encontrados = False

    for libro in libros.values():

        if termino in libro.titulo.casefold():

            mostrar_datos_libro(libro)
            encontrados = True

    if not encontrados:
        print("No se ha encontrado ningun libro.")


# Funcion para mostrar los socios que tienen libros prestados
def mostrar_prestamos(libros, socios):

    print("\n--------------- SOCIOS CON PRESTAMOS ---------------")

    encontrados = False

    for socio in socios.values():

        if socio.tiene_libro():

            codigo_libro = socio.codigo_libro
            libro = libros.get(codigo_libro)

            if libro is not None:
                print(
                    f"Socio: {socio.codigo} | {socio.nombre} | "
                    f"Libro: {libro.titulo}"
                )
            else:
                print(
                    f"Socio: {socio.codigo} | "
                    f"Libro asociado: {codigo_libro}"
                )

            encontrados = True

    if not encontrados:
        print("Actualmente no hay libros prestados.")


# Funcion para anadir un libro nuevo
def anadir_libro(libros):

    print("\n--------------- ANADIR LIBRO ---------------")

    codigo = input("Introduce el codigo del libro: ").strip().upper()

    # Comprobamos que el codigo no exista
    if not codigo:
        print("El codigo no puede estar vacio.")
        return

    if codigo in libros:
        print("Ya existe un libro con ese codigo.")
        return

    titulo = input("Introduce el titulo: ").strip()
    autor = input("Introduce el autor: ").strip()

    # Comprobamos que el ano sea numerico
    try:
        anio = int(input("Introduce el ano: "))

    except ValueError:
        print("El ano debe ser un numero.")
        return

    categoria = input("Introduce la categoria: ").strip()

    # Creamos el nuevo libro
    libro = Libro(codigo, titulo, autor, anio, categoria)

    # Lo anadimos al diccionario
    libros[codigo] = libro

    print("Libro anadido correctamente.")


# Funcion para anadir un socio nuevo
def anadir_socio(socios):

    print("\n--------------- ANADIR SOCIO ---------------")

    codigo = input("Introduce el codigo del socio: ").strip().upper()

    # Comprobamos que el codigo no exista
    if not codigo:
        print("El codigo no puede estar vacio.")
        return

    if codigo in socios:
        print("Ya existe un socio con ese codigo.")
        return

    nombre = input("Introduce el nombre: ").strip()
    email = input("Introduce el email: ").strip()

    # Creamos el nuevo socio
    socio = Socio(codigo, nombre, email)

    # Lo anadimos al diccionario
    socios[codigo] = socio

    print("Socio anadido correctamente.")


# Funcion para elegir si queremos anadir un libro o un socio
def anadir_elementos(libros, socios):

    while True:

        print("\n--------------- ANADIR ELEMENTOS ---------------")
        print("1. Anadir un libro")
        print("2. Anadir un socio")
        print("3. Volver al menu principal")

        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            anadir_libro(libros)

        elif opcion == "2":
            anadir_socio(socios)

        elif opcion == "3":
            break

        else:
            print("Opcion no valida.")


# Funcion para guardar los datos y salir
def salir_programa(libros, socios):

    guardar_libros(libros)
    guardar_socios(socios)

    print("\nDatos guardados correctamente.")
    print("Gracias por utilizar la biblioteca.")


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


# PRUEBAS TEMPORALES DE LA FASE 6

if __name__ == "__main__":

    # Cargamos los datos
    libros = cargar_libros()
    socios = cargar_socios()

    print("Biblioteca cargada correctamente.")
    print("Libros:", len(libros))
    print("Socios:", len(socios))

    # Opcion 1: mostrar todos los libros
    mostrar_libros(libros)

    # Opcion 2: mostrar libros disponibles
    mostrar_disponibles(libros)

    # Opcion 3: buscar un libro
    buscar_libro(libros)

    # Opcion 6: mostrar socios con prestamos
    mostrar_prestamos(libros, socios)

    # Opcion 7: anadir libros o socios
    anadir_elementos(libros, socios)

    print("\nPruebas de la FASE 6 finalizadas.")
