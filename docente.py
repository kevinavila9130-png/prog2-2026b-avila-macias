"""Define la clase Docente, segunda hija de Persona."""

from persona import Persona


class Docente(Persona):
    """Representa a un docente de la institución."""

    def __init__(self, nombre, numero_empleado, departamento):
        """Crea un docente y valida su número y departamento."""
        if numero_empleado is None or not str(numero_empleado).strip():
            raise ValueError("El número de empleado no puede estar vacío.")
        if not isinstance(departamento, str) or not departamento.strip():
            raise ValueError("El departamento no puede estar vacío.")

        numero = str(numero_empleado).strip()
        super().__init__(nombre, numero)
        self._numero_empleado = numero
        self._departamento = departamento.strip()

    @property
    def numero_empleado(self):
        """Devuelve el número de empleado."""
        return self._numero_empleado

    @property
    def departamento(self):
        """Devuelve el departamento del docente."""
        return self._departamento

    def describir(self):
        """Redefine la descripción para mostrar los datos del docente."""
        return (
            f"Docente: {self._nombre} | Número de empleado: "
            f"{self._numero_empleado} | Departamento: {self._departamento}"
        )
