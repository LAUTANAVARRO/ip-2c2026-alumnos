# Estos tests usan la oferta real (datos/oferta.csv) y no gastan requests: no llaman al modelo.
from sarmi import configuracion
from sarmi.capas.herramientas import herramientas


def valoresDe(respuesta, posicion):
    valores = []

    for horario in respuesta["datos"]:
        valores.append(horario[posicion])

    return valores


def testVariasMateriasPideCual():
    respuesta = herramientas.consultarMateria("programación")

    assert respuesta["estado"] == configuracion.ESTADO_VARIAS_MATERIAS


def testNombreExactoPideComision():
    respuesta = herramientas.consultarMateria("Introducción a la Programación")

    assert respuesta["estado"] == configuracion.ESTADO_FALTA_COMISION


def testConComisionDevuelveElAula():
    respuesta = herramientas.consultarMateria("Introducción a la Programación", "7")

    assert valoresDe(respuesta, configuracion.POSICION_AULA) == ["VT ASINC", "LABO COM 7118"]


def testMateriaInexistente():
    respuesta = herramientas.consultarMateria("astronomía")

    assert respuesta["estado"] == configuracion.ESTADO_MATERIA_NO_ENCONTRADA


def testAulaDevuelveLasMateriasDelDia():
    respuesta = herramientas.consultarAula("7118", "viernes")

    assert valoresDe(respuesta, configuracion.POSICION_MATERIA) == ["ANÁLISIS NUMÉRICO", "INTRODUCCIÓN A LA PROGRAMACIÓN"]


def testSuperposicion():
    respuesta = herramientas.consultarSuperposicion("Introducción a la Programación", "7", "Análisis Numérico", "1")

    assert respuesta["estado"] == configuracion.ESTADO_OK
    assert respuesta["datos"] == []
