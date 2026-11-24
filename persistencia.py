"""Funciones para guardar y recuperar el sistema mediante JSON."""

import json
from pathlib import Path

from estudiante import Estudiante
from docente import Docente
from curso import Curso


def guardar(sistema, ruta):
    """Escribe personas, cursos e inscripciones en un archivo JSON."""
    datos = {
        "personas": [],
        "cursos": []
    }

    for persona in sistema._personas.values():
        if isinstance(persona, Estudiante):
            datos["personas"].append({
                "tipo": "estudiante",
                "nombre": persona.nombre,
                "codigo": persona.codigo,
                "carrera": persona.carrera
            })
        elif isinstance(persona, Docente):
            datos["personas"].append({
                "tipo": "docente",
                "nombre": persona.nombre,
                "numero_empleado": persona.numero_empleado,
                "departamento": persona.departamento
            })

    for curso in sistema._cursos.values():
        datos["cursos"].append({
            "clave": curso.clave,
            "nombre": curso.nombre,
            "cupo_maximo": curso.cupo_maximo,
            "estudiantes_inscritos": curso.estudiantes_inscritos
        })

    destino = Path(ruta)
    destino.parent.mkdir(parents=True, exist_ok=True)
    with destino.open("w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)


def cargar(sistema, ruta):
    """Lee el JSON y reconstruye el estado; si no existe, inicia vacío."""
    origen = Path(ruta)
    if not origen.exists():
        return

    try:
        with origen.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except json.JSONDecodeError as error:
        raise ValueError("El archivo de datos no contiene JSON válido.") from error

    if not isinstance(datos, dict):
        raise ValueError("El formato del archivo de datos no es válido.")

    personas_nuevas = {}
    cursos_nuevos = {}

    for registro in datos.get("personas", []):
        tipo = registro.get("tipo")
        if tipo == "estudiante":
            persona = Estudiante(
                registro["nombre"], registro["codigo"], registro["carrera"]
            )
        elif tipo == "docente":
            persona = Docente(
                registro["nombre"],
                registro["numero_empleado"],
                registro["departamento"]
            )
        else:
            raise ValueError("El archivo contiene un tipo de persona desconocido.")

        if persona.identificador in personas_nuevas:
            raise ValueError("El archivo contiene identificadores de persona duplicados.")
        personas_nuevas[persona.identificador] = persona

    for registro in datos.get("cursos", []):
        curso = Curso(
            registro["clave"], registro["nombre"], registro["cupo_maximo"]
        )
        if curso.clave in cursos_nuevos:
            raise ValueError("El archivo contiene claves de curso duplicadas.")

        for codigo in registro.get("estudiantes_inscritos", []):
            codigo = str(codigo)
            if codigo not in personas_nuevas:
                raise ValueError(
                    f"El archivo intenta inscribir al estudiante inexistente {codigo}."
                )
            if not isinstance(personas_nuevas[codigo], Estudiante):
                raise ValueError("El archivo contiene una inscripción asociada a un docente.")
            curso.inscribir(codigo)

        cursos_nuevos[curso.clave] = curso

    sistema._personas = personas_nuevas
    sistema._cursos = cursos_nuevos
