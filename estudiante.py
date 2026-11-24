"""Define la clase Estudiante, hija de Persona."""

from persona import Persona


class Estudiante(Persona):
    """Representa a un estudiante con código y carrera."""

    def __init__(self, nombre, codigo, carrera):
        """Crea un estudiante y valida el código y la carrera."""
        codigo_texto = str(codigo).strip()
        if not codigo_texto.isdigit():
            raise ValueError("El código del estudiante debe contener únicamente números.")
        if not isinstance(carrera, str) or not carrera.strip():
            raise ValueError("La carrera no puede estar vacía; selecciona una carrera válida.")

        super().__init__(nombre, codigo_texto)
        self._codigo = codigo_texto
        self._carrera = carrera.strip()

    @property
    def codigo(self):
        """Devuelve el código del estudiante."""
        return self._codigo

    @property
    def carrera(self):
        """Devuelve la carrera del estudiante."""
        return self._carrera

    def describir(self):
        """Redefine la descripción para mostrar los datos académicos."""
        return (
            f"Estudiante: {self._nombre} | Código: {self._codigo} "
            f"| Carrera: {self._carrera}"
        )
