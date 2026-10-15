from datetime import date

class Prestamo:

    def __init__(self, usuario, libro, fecha_prestamo=None, fecha_devolucion=None):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = (fecha_prestamo if fecha_prestamo is not None else date.today())
        self.fecha_devolucion = fecha_devolucion

    @property
    def activo(self):
        return self.fecha_devolucion is None

    def __str__(self) -> str:
        estado = "Activo" if self.activo else f"Devuelto: {self.fecha_devolucion}"

        return (
            f"Nombre: {self.usuario.nombre} \n"
            f"Apellido: {self.usuario.apellido} \n"
            f"Titulo: {self.libro.titulo} \n"
            f"Fecha Prestamo: {self.fecha_prestamo} \n"
            f"Estado: {estado}"
        )

