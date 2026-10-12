import csv

from ... import configuracion


def cargarOferta():
    """Devuelve la oferta académica como lista de listas (un horario por fila), sin el encabezado."""
    filas = leerFilas(configuracion.RUTA_OFERTA)
    oferta = []

    for posicion in range(configuracion.PRIMERA_FILA_CON_DATOS, len(filas)):
        oferta.append(filas[posicion])

    return oferta


def leerFilas(ruta):
    filas = []

    with open(ruta, encoding="utf-8") as archivo:
        for fila in csv.reader(archivo):
            filas.append(fila)

    return filas
