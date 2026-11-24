"""Pruebas automatizadas del Sistema de Gestión Académica."""

from pathlib import Path
import tempfile
from estudiante import Estudiante
from docente import Docente
from curso import Curso
from sistema import Sistema


def probar_creacion_y_polimorfismo():
    """Verifica herencia, encapsulamiento y polimorfismo en describir()."""
    est = Estudiante("Ana López", "22012345", "Ciberseguridad")
    doc = Docente("Dr. Carlos Ruiz", "EMP01", "Programación II")
    cur = Curso("PROG2", "Programación II", 2)

    assert est.nombre == "Ana López"
    assert est.codigo == "22012345"
    assert est.carrera == "Ciberseguridad"
    assert "Estudiante:" in est.describir()

    assert doc.numero_empleado == "EMP01"
    assert doc.departamento == "Programación II"
    assert "Docente:" in doc.describir()

    assert "Cupo: 0/2" in cur.describir()


def probar_flujo_sistema_y_validaciones():
    """Verifica el contrato de métodos y el rechazo de casos inválidos."""
    sistema = Sistema()
    est1 = Estudiante("Kevin Ávila", "1001", "Ciberseguridad")
    est2 = Estudiante("Fátima Macías", "1002", "Ciberseguridad")
    est3 = Estudiante("Luis Pérez", "1003", "IA")
    doc1 = Docente("Martha Ulloa", "D01", "Programación II")
    curso = Curso("PROG3", "Programación III", 2)

    sistema.registrar(est1)
    sistema.registrar(est2)
    sistema.registrar(est3)
    sistema.registrar(doc1)
    sistema.registrar_curso(curso)

    # Inscripción válida
    sistema.asignar("1001", "PROG3")
    sistema.asignar("1002", "PROG3")
    assert len(curso.estudiantes_inscritos) == 2

    # Validación 1: Cupo lleno
    try:
        sistema.asignar("1003", "PROG3")
        assert False, "Debió rechazar inscripción por cupo lleno"
    except ValueError:
        pass

    # Validación 2: Estudiante duplicado en el mismo curso
    try:
        sistema.asignar("1001", "PROG3")
        assert False, "Debió rechazar inscripción duplicada"
    except ValueError:
        pass

    # Validación 3: Intentar inscribir a un docente
    try:
        sistema.asignar("D01", "PROG3")
        assert False, "Debió rechazar inscripción de un docente"
    except ValueError:
        pass

    # Validación 4: Datos vacíos o inválidos
    for accion in [
        lambda: Estudiante("", "1004", "Ciberseguridad"),
        lambda: Estudiante("Juan", "ABC", "Ciberseguridad"),
        lambda: Estudiante("Juan", "1004", ""),
        lambda: Curso("PROG3", "Repetido", 10),
    ]:
        try:
            accion()
            assert False, "Debió lanzar ValueError"
        except ValueError:
            pass

    # Cancelación válida y rechazo de cancelación inexistente
    sistema.cancelar_inscripcion("1001", "PROG3")
    assert len(curso.estudiantes_inscritos) == 1
    try:
        sistema.cancelar_inscripcion("1001", "PROG3")
        assert False, "Debió rechazar cancelar inscripción inexistente"
    except ValueError:
        pass


def probar_persistencia():
    """Verifica guardado, carga y manejo de archivo inexistente."""
    sistema = Sistema()
    sistema.registrar(Estudiante("Ana López", "2001", "Ciberseguridad"))
    sistema.registrar_curso(Curso("PROG3", "Programación III", 10))
    sistema.asignar("2001", "PROG3")

    with tempfile.TemporaryDirectory() as tmpdir:
        ruta = Path(tmpdir) / "test_datos.json"
        Sistema.guardar(sistema, ruta)

        sistema_recuperado = Sistema()
        Sistema.cargar(sistema_recuperado, ruta)
        assert "2001" in sistema_recuperado._personas
        assert "PROG3" in sistema_recuperado._cursos
        assert "2001" in sistema_recuperado._cursos["PROG3"].estudiantes_inscritos

        # Cargar archivo que no existe no debe lanzar error
        sistema_vacio = Sistema()
        Sistema.cargar(sistema_vacio, Path(tmpdir) / "no_existe.json")
        assert len(sistema_vacio._personas) == 0


if __name__ == "__main__":
    probar_creacion_y_polimorfismo()
    probar_flujo_sistema_y_validaciones()
    probar_persistencia()
    print("Todas las pruebas propias pasaron correctamente.")