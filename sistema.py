"""Contiene la clase Sistema y los cinco métodos del contrato."""

from estudiante import Estudiante
from docente import Docente
from curso import Curso


class Sistema:
    """Administra personas registradas, cursos e inscripciones."""

    def __init__(self):
        """Inicializa las colecciones internas del sistema."""
        # Diccionario que almacena personas utilizando su identificador como clave.
        self._personas = {}
        
    # Diccionario que almacena cursos utilizando su clave como identificador.
        self._cursos = {}

    def registrar(self, objeto):
        """Registra un Estudiante o Docente si su identificador no existe."""
        if not isinstance(objeto, (Estudiante, Docente)):
            raise TypeError("Solo se pueden registrar objetos Estudiante o Docente.")

        identificador = objeto.identificador
        if identificador in self._personas:
            raise ValueError(f"Ya existe una persona registrada con el identificador {identificador}.")

        # Se comprueba nuevamente el código para proteger el registro.
        if isinstance(objeto, Estudiante) and not objeto.codigo.isdigit():
            raise ValueError("El código del estudiante debe contener únicamente números.")

        self._personas[identificador] = objeto

    def asignar(self, identificador, clave):
        """Inscribe al estudiante identificado en el curso indicado."""
        identificador = str(identificador).strip()
        clave = str(clave).strip()

        if identificador not in self._personas:
            raise ValueError(f"No se encontró al estudiante con código {identificador}.")
        if not isinstance(self._personas[identificador], Estudiante):
            raise ValueError("La inscripción a cursos solo está disponible para estudiantes.")
        if clave not in self._cursos:
            raise ValueError(f"No se encontró el curso con clave {clave}.")

        self._cursos[clave].inscribir(identificador)

    def listar(self):
        """Imprime todas las personas y cursos registrados."""
        print("\n=== PERSONAS REGISTRADAS ===")
        if not self._personas:
            print("No hay personas registradas.")
        else:
            for persona in self._personas.values():
                # Polimorfismo: se ejecuta describir() según el tipo de objeto.
                print(persona.describir())

        print("\n=== CURSOS REGISTRADOS ===")
        if not self._cursos:
            print("No hay cursos registrados.")
        else:
            for curso in self._cursos.values():
                print(curso.describir())
                if curso.estudiantes_inscritos:
                    print("  Estudiantes inscritos:", ", ".join(curso.estudiantes_inscritos))

    def registrar_curso(self, curso):
        """Registra un curso y rechaza claves duplicadas."""
        if not isinstance(curso, Curso):
            raise TypeError("El objeto que se intenta registrar no es un Curso.")
        if curso.clave in self._cursos:
            raise ValueError(f"La clave del curso {curso.clave} ya existe.")
        self._cursos[curso.clave] = curso

    def cancelar_inscripcion(self, identificador, clave):
        """Cancela la inscripción de un estudiante en un curso."""
        identificador = str(identificador).strip()
        clave = str(clave).strip()

        if identificador not in self._personas:
            raise ValueError(f"No se encontró al estudiante con código {identificador}.")
        if not isinstance(self._personas[identificador], Estudiante):
            raise ValueError("Solo se puede cancelar la inscripción de un estudiante.")
        if clave not in self._cursos:
            raise ValueError(f"No se encontró el curso con clave {clave}.")

        self._cursos[clave].cancelar_inscripcion(identificador)

    @staticmethod
    def guardar(sistema, ruta):
        """Guarda el estado del sistema en la ruta indicada."""
        from persistencia import guardar
        guardar(sistema, ruta)

    @staticmethod
    def cargar(sistema, ruta):
        """Carga el estado guardado dentro de una instancia existente."""
        from persistencia import cargar
        cargar(sistema, ruta)
