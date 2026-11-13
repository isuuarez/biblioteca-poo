
class ErrorBiblioteca(Exception):

    def __init__(self, codigo, mensaje):
        self.codigo = codigo
        self.mensaje = mensaje

        super().__init__(mensaje)
