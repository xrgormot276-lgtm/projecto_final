class Usuario:

    def __init__(self, id, nombre, apellido, email):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def __str__(self) -> str:
        return f"Id: {self.id} - Nombre Completo: {self.nombre} {self.apellido} - Email: {self.email}"

    def __eq__(self, __value: object) -> bool:
            return self.id == __value.id
