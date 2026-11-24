"""Define la clase base Persona del sistema académico."""


class Persona:
    """Representa los datos generales compartidos por estudiantes y docentes."""

    def __init__(self, nombre, identificador):
        """Inicializa una persona y valida sus datos básicos."""
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if identificador is None or not str(identificador).strip():
            raise ValueError("El identificador no puede estar vacío.")

        self._nombre = nombre.strip()
        self._identificador = str(identificador).strip()

    @property
    def nombre(self):
        """Devuelve el nombre de la persona."""
        return self._nombre

    @property
    def identificador(self):
        """Devuelve el identificador de la persona."""
        return self._identificador

    def describir(self):
        """Devuelve una descripción general de la persona."""
        return f"Persona: {self._nombre} (ID: {self._identificador})"
