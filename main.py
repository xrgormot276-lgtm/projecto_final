from modelos.libro import Libro
from modelos.usuario import Usuario
from modelos.prestamo import Prestamo
from servicios.biblioteca import Biblioteca

#GitHub Publico: https://github.com/xrgormot276-lgtm/projecto_final y solo falta control excepciones , controlar archivos y readme.

def menu():

    print()
    print("=================================")
    print("GESTIÓN DE BIBLIOTECA")
    print("=================================")
    print("1. Registrar libro")
    print("2. Registrar usuario")
    print("3. Buscar libro")
    print("4. Listar libros")
    print("5. Realizar préstamo")
    print("6. Registrar devolución")
    print("7. Mostrar préstamos activos")
    print("8. Mostrar préstamos de un usuario")
    print("9. Guardar datos")
    print("0. Salir")
    print("=================================")

def registrar_libro(biblioteca):
    isbn = input("ISBN: ").strip()
    titulo = input("Titulo: ").strip()
    autor = input("Autor: ").strip()
    anio = input("Año: ").strip()
    genero = input("Genero: ").strip()

    libro = Libro(isbn, titulo, autor, anio, genero)
    biblioteca.resgristrar_libro(libro)

def registrar_usuario(biblioteca):
    id = input("ID: ").strip()
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    email = input("Email: ").strip()

    usuario = Usuario(id, nombre, apellido, email)
    biblioteca.resgristrar_usuario(usuario)

def registrar_prestamo(biblioteca):
    id = input("ID del usuario: ").strip()
    isbn = input("ISBN del libro: ").strip()
    fecha_prestamo = input("Fecha del prestamo: ").strip()

    if fecha_prestamo == "":
        fecha_prestamo = None

    if biblioteca.buscar_usuario_id(id) and biblioteca.buscar_libro_isbn(isbn):
        if biblioteca.libro_disponible(isbn):
            biblioteca.resgristrar_prestamo(id, isbn, fecha_prestamo)
                        
            print("Préstamo realizado correctamente.")
        else:
            print("Error: El libro ya esta prestado.")
    else:
        print("Error: El usuario o el libro no existen")

def registrar_devolucion(biblioteca):
    isbn = input("ISBN del libro a buscar: ").strip()
    fecha_prestamo = input("Fecha del prestamo a buscar: ").strip()
    fecha_devolucion = input("Fecha de la devolucion: ").strip()

    biblioteca.devolver_libro(isbn, fecha_prestamo, fecha_devolucion)

def buscar_libro(biblioteca):
    print("=======================================")
    print("Buscar libro")
    print("=======================================")
    print("1. Buscar un libro por su identificador")
    print("2. Buscar libros por título")
    print("3. Buscar libros por autor")
    print("=======================================")
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        isbn = input("Escribe el ISBN del libro: ").strip()

        return biblioteca.buscar_libro_isbn(isbn)
    
    elif opcion == 2:
        titulo = input("Escribe el Titulo del libro: ").strip()

        return biblioteca.buscar_libro_titulo(titulo)
                
    elif opcion == 3:
        autor = input("Escribe el autor del libro: ").strip()

        return biblioteca.buscar_libro_autor(autor)

    else:
        print("Error: Escribe las opciones entre 1-3.")

def main():
    biblioteca = Biblioteca()

    while True:

        menu()
        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            registrar_libro(biblioteca)

        elif opcion == 2:
            registrar_usuario(biblioteca)
            
        elif opcion == 3:
            print(buscar_libro(biblioteca))

        elif opcion == 4:
            biblioteca.listar_libros()

        elif opcion == 5:
            registrar_prestamo(biblioteca)

        elif opcion == 6:
            registrar_devolucion(biblioteca)

        elif opcion == 7:
            biblioteca.mostrar_prestamo_activo()

        elif opcion == 8:
            biblioteca.mostrar_prestamo_usuario()

        elif opcion == 9:
            pass

        elif opcion == 0:
            break
        else:
            print("Error: Escribe las opciones entre 0-9.")

if __name__ == "__main__":
    main()