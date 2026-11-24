"""Define la clase Curso y administra sus inscripciones."""


class Curso:
    """Representa una asignatura con un cupo máximo de estudiantes."""

    def __init__(self, clave, nombre, cupo_maximo):
        """Crea un curso y comprueba que sus datos sean válidos."""
        if clave is None or not str(clave).strip():
            raise ValueError("La clave del curso no puede estar vacía.")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del curso no puede estar vacío.")
        if isinstance(cupo_maximo, bool) or not isinstance(cupo_maximo, int) or cupo_maximo <= 0:
            raise ValueError("El cupo máximo debe ser un número entero mayor que cero.")

        self._clave = str(clave).strip()
        self._nombre = nombre.strip()
        self._cupo_maximo = cupo_maximo
        self._estudiantes_inscritos = []

    @property
    def clave(self):
        """Devuelve la clave del curso."""
        return self._clave

    @property
    def nombre(self):
        """Devuelve el nombre del curso."""
        return self._nombre

    @property
    def cupo_maximo(self):
        """Devuelve el cupo máximo del curso."""
        return self._cupo_maximo

    @property
    def estudiantes_inscritos(self):
        """Devuelve una copia de los códigos inscritos."""
        return list(self._estudiantes_inscritos)

    def inscribir(self, codigo):
        """Agrega un código al curso si no está repetido y hay cupo."""
        codigo = str(codigo)
        if codigo in self._estudiantes_inscritos:
            raise ValueError("El estudiante ya está inscrito en este curso.")
        if len(self._estudiantes_inscritos) >= self._cupo_maximo:
            raise ValueError("No hay cupo disponible en este curso.")
        self._estudiantes_inscritos.append(codigo)

    def cancelar_inscripcion(self, codigo):
        """Elimina una inscripción existente o informa que no existe."""
        codigo = str(codigo)
        if codigo not in self._estudiantes_inscritos:
            raise ValueError("El estudiante no está inscrito en esta asignatura.")
        self._estudiantes_inscritos.remove(codigo)

    def describir(self):
        """Devuelve un resumen del curso y de su ocupación."""
        ocupados = len(self._estudiantes_inscritos)
        return (
            f"Curso: {self._nombre} | Clave: {self._clave} "
            f"| Cupo: {ocupados}/{self._cupo_maximo}"
        )
