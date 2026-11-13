
# Importamos las clases necesarias
from modelo.libro import Libro
from modelo.socio import Socio

from dao.libro_dao import LibroDAO
from dao.socio_dao import SocioDAO

from servicios.biblioteca import Biblioteca
from errores.excepciones import ErrorBiblioteca


# Rutas de los archivos
RUTA_LIBROS = "datos/libros.txt"
RUTA_SOCIOS = "datos/socios.txt"


# Funcion para mostrar el menu principal
def mostrar_menu():

    print("\n================================")
    print("          BIBLIOTECA")
    print("================================")

    print("1. Mostrar todos los libros")
    print("2. Mostrar libros disponibles")
    print("3. Buscar libro")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Mostrar socios con prestamos")
    print("7. Añadir libros y socios")
    print("8. Salir")

    print("================================")


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


# Opcion 1: mostrar todos los libros
def opcion_mostrar_libros(biblioteca):

    print("\n----- TODOS LOS LIBROS -----")

    libros = biblioteca.obtener_todos_los_libros()

    for libro in libros:
        mostrar_datos_libro(libro)


# Opcion 2: mostrar libros disponibles
def opcion_mostrar_disponibles(biblioteca):

    print("\n----- LIBROS DISPONIBLES -----")

    libros = biblioteca.obtener_libros_disponibles()

    if not libros:
        print("No hay libros disponibles.")
        return

    for libro in libros:
        mostrar_datos_libro(libro)


# Opcion 3: buscar un libro
def opcion_buscar_libro(biblioteca):

    termino = input("Introduce el titulo o una parte del titulo: ")

    libros = biblioteca.buscar_libros(termino)

    if not libros:
        print("No se ha encontrado ningun libro.")
        return

    print("\n----- RESULTADOS DE LA BUSQUEDA -----")

    for libro in libros:
        mostrar_datos_libro(libro)


# Opcion 4: prestar un libro
def opcion_prestar_libro(biblioteca):

    codigo_libro = input("Introduce el codigo del libro: ")
    codigo_socio = input("Introduce el codigo del socio: ")

    try:

        libro = biblioteca.prestar_libro(codigo_libro, codigo_socio)

        print("Prestamo realizado correctamente.")
        print("Libro:", libro.titulo)

    except ErrorBiblioteca as error:

        print("ERROR:", error.mensaje)
        print("Codigo:", error.codigo)


# Opcion 5: devolver un libro
def opcion_devolver_libro(biblioteca):

    codigo_socio = input("Introduce el codigo del socio: ")

    try:

        libro = biblioteca.devolver_libro(codigo_socio)

        print("Devolucion realizada correctamente.")
        print("Libro devuelto:", libro.titulo)

    except ErrorBiblioteca as error:

        print("ERROR:", error.mensaje)
        print("Codigo:", error.codigo)


# Opcion 6: mostrar socios con libros prestados
def opcion_mostrar_prestamos(biblioteca):

    print("\n----- SOCIOS CON PRESTAMOS -----")

    prestamos = biblioteca.obtener_socios_con_prestamos()

    if not prestamos:
        print("Actualmente no hay libros prestados.")
        return

    for socio, libro in prestamos:

        if libro is not None:

            print(
                f"Socio: {socio.codigo} | {socio.nombre} | "
                f"Libro: {libro.titulo}"
            )


# Opcion 7: añadir libros y socios
def opcion_anadir_elementos(biblioteca):

    while True:

        print("\n----- AÑADIR ELEMENTOS -----")
        print("1. Añadir libro")
        print("2. Añadir socio")
        print("3. Volver al menu principal")

        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":

            codigo = input("Codigo del libro: ").strip().upper()

            titulo = input("Titulo: ").strip()
            autor = input("Autor: ").strip()

            try:
                anio = int(input("Ano: "))

            except ValueError:
                print("El ano debe ser numerico.")
                continue

            categoria = input("Categoria: ").strip()

            if not codigo or not titulo or not autor or not categoria:
                print("Todos los campos son obligatorios.")
                continue

            libro = Libro(codigo, titulo, autor, anio, categoria)

            if biblioteca.anadir_libro(libro):
                print("Libro añadido correctamente.")
            else:
                print("Ya existe un libro con ese codigo.")

        elif opcion == "2":

            codigo = input("Codigo del socio: ").strip().upper()
            nombre = input("Nombre: ").strip()
            email = input("Email: ").strip()

            if not codigo or not nombre or not email:
                print("Todos los campos son obligatorios.")
                continue

            socio = Socio(codigo, nombre, email)

            if biblioteca.anadir_socio(socio):
                print("Socio añadido correctamente.")
            else:
                print("Ya existe un socio con ese codigo.")

        elif opcion == "3":

            break

        else:

            print("Opcion no valida.")


# Funcion principal del programa
def main():

    # Creamos los DAO
    libro_dao = LibroDAO(RUTA_LIBROS)
    socio_dao = SocioDAO(RUTA_SOCIOS)

    # Creamos la biblioteca
    biblioteca = Biblioteca(libro_dao, socio_dao)

    # Cargamos los datos
    biblioteca.cargar_datos()

    print("\nInformacion de los libros cargada correctamente.")
    print("Libros cargados:", len(biblioteca.obtener_todos_los_libros()))
    print("Socios cargados:", len(biblioteca.obtener_todos_los_socios()))

    # Bucle del menu principal
    while True:

        mostrar_menu()

        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":

            opcion_mostrar_libros(biblioteca)

        elif opcion == "2":

            opcion_mostrar_disponibles(biblioteca)

        elif opcion == "3":

            opcion_buscar_libro(biblioteca)

        elif opcion == "4":

            opcion_prestar_libro(biblioteca)

        elif opcion == "5":

            opcion_devolver_libro(biblioteca)

        elif opcion == "6":

            opcion_mostrar_prestamos(biblioteca)

        elif opcion == "7":

            opcion_anadir_elementos(biblioteca)

        elif opcion == "8":

            biblioteca.guardar_datos()

            print("\nDatos guardados correctamente.")
            print("Gracias por utilizar la biblioteca.")

            break

        else:

            print("Opcion no valida. Introduce un numero del 1 al 8.")


# Iniciamos el programa
if __name__ == "__main__":
    main()
