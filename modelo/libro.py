
class Libro:

    def __init__(self, codigo, titulo, autor, anio, categoria, codigo_socio=None):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.categoria = categoria
        self.codigo_socio = codigo_socio

    # Comprobar si el libro esta disponible
    def esta_disponible(self):
        return self.codigo_socio is None

    # Asignar el libro a un socio
    def asignar_socio(self, codigo_socio):
        self.codigo_socio = codigo_socio

    # Liberar el libro cuando se devuelve
    def liberar(self):
        self.codigo_socio = None
