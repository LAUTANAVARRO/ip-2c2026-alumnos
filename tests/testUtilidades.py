from sarmi.capas.utilidades import horas, listas, textos


def testEsta():
    assert listas.esta("COM-07", ["COM-01", "COM-07"])
    assert not listas.esta("COM-09", ["COM-01", "COM-07"])
    assert not listas.esta("COM-01", [])


def testCopiarListaDevuelveOtraListaIgual():
    original = [1, 2, 3]
    copia = listas.copiarLista(original)

    assert copia == [1, 2, 3]

    copia.append(4)
    assert original == [1, 2, 3]


def testNormalizarQuitaTildesYMayusculas():
    assert textos.normalizar("Introducción a la PROGRAMACIÓN") == "introduccion a la programacion"


def testContiene():
    assert textos.contiene("introduccion a la programacion", "program")
    assert not textos.contiene("algebra", "programacion")
    assert textos.contiene("algebra", "")


def testExtraerNumero():
    assert textos.extraerNumero("COM-07") == 7
    assert textos.extraerNumero("comisión 15") == 15
    assert textos.extraerNumero("sin número") == -1


def testHoraAMinutos():
    assert horas.horaAMinutos("00:00") == 0
    assert horas.horaAMinutos("18:30") == 1110
