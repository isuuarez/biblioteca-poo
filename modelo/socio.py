
class Socio:

    def __init__(self, codigo, nombre, email, codigo_libro=None):
        self.codigo = codigo
        self.nombre = nombre
        self.email = email
        self.codigo_libro = codigo_libro

    # Comprobar si el socio tiene algun libro
    def tiene_libro(self):
        return self.codigo_libro is not None

    # Asignar un libro al socio
    def asignar_libro(self, codigo_libro):
        self.codigo_libro = codigo_libro

    # Dejar al socio sin libro
    def liberar_libro(self):
        self.codigo_libro = None
