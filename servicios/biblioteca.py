from modelos.libro import Libro
from modelos.usuario import Usuario
from modelos.prestamo import Prestamo

class Biblioteca:

    def __init__(self) -> None:
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def resgristrar_usuario(self, usuario_nuevo):
            if self.buscar_usuario(usuario_nuevo):
                print("El usuario ya esta en la lista")
                return 
    
            self.usuarios.append(usuario_nuevo)

    def resgristrar_libro(self, libro_nuevo):
        if self.buscar_libro(libro_nuevo):
            print("El libro ya esta en la lista")
            return 

        self.libros.append(libro_nuevo)

    def resgristrar_prestamo(self, id, isbn, fecha_prestamo):

        usuario_nuevo = self.buscar_usuario_id(id)
        libro_nuevo = self.buscar_libro_isbn(isbn)

        for libro in self.libros:
            if libro.isbn == isbn:
                libro.disponible = False

        prestamo = Prestamo(usuario_nuevo, libro_nuevo, fecha_prestamo)
        self.prestamos.append(prestamo)

    def devolver_libro(self, isbn, fecha_prestamo, fecha_devolucion):
        prestamo_encontrado = False
        cod_libro = ""

        for prestamo in self.prestamos:
            if prestamo.libro.isbn == isbn and str(prestamo.fecha_prestamo) == fecha_prestamo and prestamo.fecha_devolucion is None:
                prestamo.fecha_devolucion = fecha_devolucion
                cod_libro = prestamo.libro.isbn

                prestamo_encontrado = True

        if prestamo_encontrado:

            for libro in self.libros:
                if libro.isbn == isbn:
                    libro.disponible = True

            print(f"Código del libro: {cod_libro}")
            print("Libro devuelto correctamente.")
        else:
            print("Error el prestamo no ha sido encontrado.")

    def mostrar_prestamo_activo(self):
        print("Prestamos Activos: ")

        for prestamo in self.prestamos:
            if prestamo.fecha_devolucion is None:
                print(prestamo)

    def mostrar_prestamo_usuario(self):
        usuario = input("ID del usuario: ").strip()

        if self.buscar_usuario_id(usuario):
            print(f"Usuario {usuario}: ")    

            for prestamo in self.prestamos:
                if prestamo.usuario.id == usuario:
                    print(prestamo)

    def libro_disponible(self, isbn):

        if self.buscar_libro_isbn(isbn).disponible:
            return True
        else:
            return False

    def buscar_libro(self, libro_nuevo):

        for libro in self.libros:
            if libro.__eq__(libro_nuevo):
                return libro

        return None

    def buscar_libro_isbn(self, isbn):

        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        
        return None

    def buscar_usuario_id(self, id):
    
            for usuario in self.usuarios:
                if usuario.id == id:
                    return usuario
            
            return None
         
    def buscar_libro_titulo(self, libro_nuevo):

        for libro in self.libros:
            if libro.titulo == libro_nuevo:
                return libro
        
        return None
             
    def buscar_libro_autor(self, libro_nuevo):

        for libro in self.libros:
            if libro.autor == libro_nuevo:
                return libro
        
        return None         

    def buscar_usuario(self, usuario_nuevo):
    
            for usuario in self.usuarios:
                if usuario.__eq__(usuario_nuevo):
                    return usuario
    
            return None

    def listar_libros(self):
        print("Libros: ")

        for libro in self.libros:
            print(libro)
