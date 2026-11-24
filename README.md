# Hito 2 – Sistema de gestión académica

**Materia:** Programación II  
**Integrantes:** Kevin Ávila Collazo y Fátima Giselle Macías Alcalá

## Descripción

El programa permite registrar estudiantes y docentes, crear cursos, inscribir estudiantes en asignaturas, cancelar inscripciones y consultar los registros. La información se conserva en un archivo JSON para que pueda recuperarse al iniciar el programa nuevamente.

## Archivos

- `persona.py`: clase padre `Persona`.
- `estudiante.py`: clase hija `Estudiante`.
- `docente.py`: clase hija `Docente`.
- `curso.py`: cursos, cupo máximo e inscripciones.
- `sistema.py`: administración de registros y métodos del contrato.
- `persistencia.py`: funciones para guardar y cargar información.
- `main.py`: menú para probar el sistema.

Todos los archivos `.py` y este README deben quedar directamente en la raíz del ZIP.

## Requisitos

- Python 3.8 o superior.
- No requiere instalar librerías externas.

## Cómo ejecutar

Abre una terminal en la carpeta donde se encuentran los archivos y ejecuta:

```bash
python3 main.py
```

En Windows también se puede ejecutar:

```bash
python main.py
```

El programa crea `datos_academicos.json` al guardar por primera vez. Si el archivo todavía no existe, el sistema inicia vacío sin producir un error. Este archivo se genera durante el uso y **no debe incluirse en el ZIP de entrega**.

## Métodos del contrato

Los nombres se conservan exactamente:

- `registrar(objeto)`: registra un objeto `Estudiante` o `Docente`.
- `asignar(identificador, clave)`: inscribe a un estudiante en un curso.
- `listar()`: imprime las personas y los cursos registrados.
- `guardar(sistema, ruta)`: guarda el estado del sistema.
- `cargar(sistema, ruta)`: recupera el estado en una instancia existente.

Los métodos `guardar` y `cargar` están disponibles como métodos estáticos de `Sistema` y sus funciones de implementación están en `persistencia.py`.

Ejemplo de uso:

```python
from sistema import Sistema
from estudiante import Estudiante
from curso import Curso

sistema = Sistema()
sistema.registrar(Estudiante("Ana López", "12345", "Ciberseguridad"))
sistema.registrar_curso(Curso("PROG101", "Programación", 25))
sistema.asignar("12345", "PROG101")
sistema.listar()

Sistema.guardar(sistema, "datos_academicos.json")
```

Para recuperar los datos:

```python
sistema_nuevo = Sistema()
Sistema.cargar(sistema_nuevo, "datos_academicos.json")
sistema_nuevo.listar()
```

## Validaciones implementadas

1. No permite registrar personas con el nombre vacío.
2. El código de estudiante debe contener únicamente números.
3. No permite crear estudiantes con carrera vacía.
4. No permite cancelar una asignatura en la que el estudiante no está inscrito.
5. Rechaza claves de curso duplicadas.
6. Rechaza inscripciones de estudiantes inexistentes.
7. No permite inscribir a un estudiante dos veces en el mismo curso.
8. No permite superar el cupo máximo del curso.
9. Rechaza identificadores de persona duplicados.

Las operaciones inválidas lanzan excepciones con mensajes que explican el motivo. El menú de `main.py` captura esos mensajes para que el programa pueda continuar.

## Conceptos de programación orientada a objetos

- **Herencia:** `Estudiante` y `Docente` heredan de `Persona`.
- **Polimorfismo:** ambas clases redefinen `describir()` y `listar()` utiliza ese método sin necesitar distinguir manualmente cómo describir cada tipo.
- **Encapsulamiento:** los atributos internos se identifican con guion bajo, por ejemplo `_nombre`, `_carrera` y `_cupo_maximo`.
- **Composición:** `Sistema` administra una colección de cursos.
- **Persistencia:** se utiliza JSON para guardar y reconstruir personas, cursos e inscripciones.

## Pruebas recomendadas antes de entregar

1. Ejecutar `python3 main.py` sin que exista `datos_academicos.json`.
2. Registrar un estudiante y un docente.
3. Registrar un curso e inscribir al estudiante.
4. Intentar registrar un código no numérico y una carrera vacía.
5. Intentar registrar dos cursos con la misma clave.
6. Intentar cancelar una materia en la que el estudiante no está inscrito.
7. Cerrar el programa y volver a ejecutarlo; comprobar que los registros siguen ahí.
8. Borrar `datos_academicos.json` y comprobar que el programa inicia normalmente.

## Preparación del ZIP

El ZIP debe contener los archivos `.py` y `README.md` directamente en la raíz. No incluir `__pycache__` ni `datos_academicos.json`.
