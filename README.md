
# Sistema de gestion de biblioteca

## 1. Descripcion del proyecto

Este proyecto consiste en desarrollar un sistema de gestion de biblioteca utilizando Python y Programacion Orientada a Objetos (POO).

La aplicacion permite gestionar los libros y socios de una biblioteca, realizar prestamos y devoluciones, consultar la disponibilidad de los libros y almacenar la informacion en archivos TXT.

El proyecto utiliza una arquitectura modular para separar las clases, el acceso a los datos, la logica de negocio y la interfaz de usuario.

## 2. Tecnologias utilizadas

- Python 3.
- Programacion Orientada a Objetos.
- Archivos TXT para almacenar los datos.
- Git y GitHub para el control de versiones.

No es necesario instalar librerias externas. El proyecto utiliza modulos incluidos en Python.

## 3. Estructura del proyecto

```text
biblioteca-poo/
│
├── modelo/
│   ├── __init__.py
│   ├── libro.py
│   └── socio.py
│
├── dao/
│   ├── __init__.py
│   ├── libro_dao.py
│   └── socio_dao.py
│
├── servicios/
│   ├── __init__.py
│   └── biblioteca.py
│
├── errores/
│   ├── __init__.py
│   └── excepciones.py
│
├── datos/
│   ├── libros.txt
│   └── socios.txt
│
├── main.py
├── log.txt
└── README.md
```

## 4. Arquitectura del programa

El proyecto esta organizado en diferentes carpetas para separar responsabilidades.

### Modelo

Contiene las clases principales del programa:

- Libro: representa un libro de la biblioteca.
- Socio: representa a un socio de la biblioteca.

### DAO (Data Access Object)

Se encarga del acceso y almacenamiento de los datos.

- LibroDAO: gestiona las operaciones CRUD de los libros.
- SocioDAO: gestiona las operaciones CRUD de los socios.

CRUD significa crear, consultar, actualizar y eliminar registros.

Los DAO realizan la lectura y escritura de los archivos TXT.

### Servicios

Contiene la clase Biblioteca, que gestiona la logica de negocio:

- Realizar prestamos.
- Realizar devoluciones.
- Buscar libros.
- Obtener libros disponibles.
- Consultar socios con prestamos.
- Anadir libros y socios.
- Registrar la actividad de la biblioteca.

### Errores

Contiene la excepcion personalizada ErrorBiblioteca, utilizada para controlar los errores de la aplicacion.

### Main

Es el archivo principal del programa.

Se encarga de mostrar el menu, solicitar los datos al usuario y llamar a los metodos de la clase Biblioteca.

## 5. Funcionalidades

La aplicacion dispone de las siguientes opciones:

1. Mostrar todos los libros.
2. Mostrar libros disponibles.
3. Buscar libros por cualquier parte del titulo, independientemente de mayusculas y minusculas.
4. Prestar un libro a un socio.
5. Devolver el libro de un socio.
6. Mostrar los socios que tienen libros prestados.
7. Anadir nuevos libros y socios.
8. Guardar los datos y salir del programa.

El sistema controla diferentes situaciones, como intentar prestar un libro que ya esta ocupado o prestar un segundo libro a un socio que ya tiene uno.

## 6. Almacenamiento de datos

La informacion se almacena en dos archivos TXT:

- datos/libros.txt
- datos/socios.txt

Los archivos contienen inicialmente los datos de los libros y socios de la biblioteca.

Los cambios realizados durante la ejecucion se guardan al seleccionar la opcion 8 del menu.

## 7. Registro de actividad

El programa dispone de un archivo llamado log.txt.

En este archivo se registran las operaciones importantes, como los prestamos y las devoluciones.

El formato utilizado es:

[Fecha][Nombre del evento][Detalles]

Ejemplo:

[2026-11-13 18:30:00][PRESTAMO][Libro L001 prestado al socio S001]

## 8. Instalacion y ejecucion

### Requisitos

- Tener Python 3 instalado.
- Descargar o clonar el repositorio.
- Disponer de los archivos TXT incluidos en la carpeta datos.

### Descargar el proyecto

Se puede clonar el repositorio utilizando:

```bash
git clone https://github.com/isuarez/biblioteca-poo.git
```

Entrar en la carpeta del proyecto:

```bash
cd biblioteca-poo
```

### Ejecutar el programa

Desde la carpeta principal del proyecto ejecutar:

```bash
python main.py
```

A continuacion aparecera el menu principal de la biblioteca.

No es necesario instalar dependencias adicionales.

## 9. Posibles mejoras futuras

Aunque la aplicacion cumple las funcionalidades solicitadas, se podrian incorporar diferentes mejoras:

- Permitir que un socio tenga varios libros prestados.
- Incorporar fechas de prestamo y devolucion.
- Anadir un sistema de usuarios y contrasenas.
- Incorporar una interfaz grafica para facilitar el uso de la aplicacion.
- Permitir filtrar los libros por autor, categoria o ano.
- Utilizar una base de datos para almacenar la informacion en lugar de archivos TXT.
- Incorporar un sistema de reservas de libros.
- Anadir un control de devoluciones fuera de plazo.

Estas mejoras permitirian ampliar las funcionalidades y facilitar la gestion de la biblioteca.

## 10. Autor y repositorio

Proyecto realizado como trabajo final de Programacion Orientada a Objetos.

Repositorio GitHub:

https://github.com/isuarez/biblioteca-poo
