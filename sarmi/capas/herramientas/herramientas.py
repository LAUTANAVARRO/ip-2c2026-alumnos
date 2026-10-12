# Estas son las funciones que el modelo puede pedir que se ejecuten.
# ADK le manda al modelo el nombre y el docstring de cada una: con eso el modelo decide cuál usar.
# Por eso acá los docstrings son obligatorios.
# El modelo puede mandar un número (7) en lugar de un texto ("7"): str() lo convierte siempre a texto.
from ... import configuracion
from ..persistencia import repositorio
from ..servicios import aulas, consultas, turnos


def consultarMateria(materia, comision=""):
    """Busca en qué días, horarios y aulas se dicta una materia.

    Args:
        materia: nombre o parte del nombre de la materia.
        comision: número de comisión. Vacío si el usuario no la dijo.
    """
    oferta = repositorio.cargarOferta()

    return consultas.buscarHorarios(oferta, str(materia), str(comision))


def consultarAula(aula, dia):
    """Muestra qué materias se dictan en un aula un día, ordenadas por hora.

    Args:
        aula: número o nombre del aula, por ejemplo "7118".
        dia: día de la semana, por ejemplo "Viernes".
    """
    oferta = repositorio.cargarOferta()
    horarios = aulas.horariosEnAula(oferta, str(aula), str(dia))
    horariosOrdenados = aulas.ordenarPorHora(horarios)

    return consultas.armarRespuesta(configuracion.ESTADO_OK, horariosOrdenados)


def consultarSuperposicion(materiaA, comisionA, materiaB, comisionB):
    """Indica si dos comisiones de materias distintas se superponen en día y horario.

    Args:
        materiaA: nombre de la primera materia.
        comisionA: comisión de la primera materia.
        materiaB: nombre de la segunda materia.
        comisionB: comisión de la segunda materia.
    """
    oferta = repositorio.cargarOferta()

    return consultas.buscarSuperposicion(oferta, str(materiaA), str(comisionA), str(materiaB), str(comisionB))


def consultarTurno(materia, turno):
    """Muestra las comisiones de una materia que se dictan en un turno.

    Args:
        materia: nombre o parte del nombre de la materia.
        turno: "mañana", "tarde" o "noche".
    """
    oferta = repositorio.cargarOferta()
    horarios = consultas.horariosDeMateria(oferta, str(materia))
    horariosDelTurno = turnos.filtrarPorTurno(horarios, str(turno))

    return consultas.armarRespuesta(configuracion.ESTADO_OK, horariosDelTurno)
