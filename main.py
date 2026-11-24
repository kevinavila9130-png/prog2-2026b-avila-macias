"""Punto de entrada: menú de prueba del sistema académico."""

from pathlib import Path

from estudiante import Estudiante
from docente import Docente
from curso import Curso
from sistema import Sistema


RUTA_DATOS = Path(__file__).with_name("datos_academicos.json")


def mostrar_menu():
    """Imprime las opciones disponibles."""
    print("\n===== SISTEMA DE GESTIÓN ACADÉMICA =====")
    print("1. Registrar estudiante")
    print("2. Registrar docente")
    print("3. Registrar curso")
    print("4. Inscribir estudiante en curso")
    print("5. Cancelar inscripción")
    print("6. Listar registros")
    print("7. Guardar y salir")


def ejecutar():
    """Carga los datos, ejecuta el menú y guarda los cambios."""
    sistema = Sistema()

    try:
        Sistema.cargar(sistema, RUTA_DATOS)
        print("Datos anteriores cargados correctamente.")
    except (ValueError, KeyError, TypeError) as error:
        print(f"No se pudieron cargar los datos: {error}")
        print("El sistema iniciará con registros vacíos.")

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        try:
            if opcion == "1":
                nombre = input("Nombre completo: ")
                codigo = input("Código numérico: ")
                carrera = input("Carrera: ")
                sistema.registrar(Estudiante(nombre, codigo, carrera))
                print("Estudiante registrado correctamente.")

            elif opcion == "2":
                nombre = input("Nombre completo: ")
                numero = input("Número de empleado: ")
                departamento = input("Departamento: ")
                sistema.registrar(Docente(nombre, numero, departamento))
                print("Docente registrado correctamente.")

            elif opcion == "3":
                clave = input("Clave del curso: ")
                nombre = input("Nombre del curso: ")
                cupo = int(input("Cupo máximo (entero): "))
                sistema.registrar_curso(Curso(clave, nombre, cupo))
                print("Curso registrado correctamente.")

            elif opcion == "4":
                codigo = input("Código del estudiante: ")
                clave = input("Clave del curso: ")
                sistema.asignar(codigo, clave)
                print("Inscripción realizada correctamente.")

            elif opcion == "5":
                codigo = input("Código del estudiante: ")
                clave = input("Clave del curso: ")
                sistema.cancelar_inscripcion(codigo, clave)
                print("Inscripción cancelada correctamente.")

            elif opcion == "6":
                sistema.listar()

            elif opcion == "7":
                Sistema.guardar(sistema, RUTA_DATOS)
                print("Información guardada. Hasta pronto.")
                break

            else:
                print("Opción no válida. Selecciona una opción del 1 al 7.")

            if opcion in {"1", "2", "3", "4", "5"}:
                Sistema.guardar(sistema, RUTA_DATOS)

        except (ValueError, TypeError) as error:
            print(f"Operación rechazada: {error}")
        except (OSError, OverflowError) as error:
            print(f"No se pudo completar la operación: {error}")


if __name__ == "__main__":
    ejecutar()
