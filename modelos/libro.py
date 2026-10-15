class Libro:

    def __init__(self, isbn, titulo, autor, genero, anio=None, disponible=True):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
        self.disponible = disponible

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "Prestado"
        return f"ISBN: {self.isbn} - Titulo: {self.titulo} - Disponible: {estado}"

    def __eq__(self, __value: object) -> bool:
        return self.isbn == __value.isbn