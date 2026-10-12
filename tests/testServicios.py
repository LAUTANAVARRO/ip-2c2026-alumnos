from sarmi.capas.servicios import aulas, materias, superposiciones

PROGRAMACION_07 = ["A0444", "INTRODUCCIÓN A LA PROGRAMACIÓN", "COM-07", "", "", "Viernes", "18:00", "22:00", "LABO COM 7118", "", "", "", "", ""]
PROGRAMACION_07_VIRTUAL = ["A0444", "INTRODUCCIÓN A LA PROGRAMACIÓN", "COM-07", "", "", "VT ASINC", "", "", "VT ASINC", "", "", "", "", ""]
PROGRAMACION_13 = ["A0444", "INTRODUCCIÓN A LA PROGRAMACIÓN", "COM-13", "", "", "Viernes", "13:00", "16:59", "LABO COM 7145", "", "", "", "", ""]
ALGEBRA_02 = ["A0023", "ALGEBRA I", "COM-02", "", "", "Viernes", "20:00", "22:00", "AULA 7177", "", "", "", "", ""]
OFERTA = [PROGRAMACION_07, PROGRAMACION_07_VIRTUAL, PROGRAMACION_13, ALGEBRA_02]
POSICION_COMISION = 2


def testValoresDistintos():
    assert materias.valoresDistintos(OFERTA, POSICION_COMISION) == ["COM-07", "COM-13", "COM-02"]


def testBuscarMateriaSinTildes():
    assert materias.buscarMateria(OFERTA, "programacion") == [PROGRAMACION_07, PROGRAMACION_07_VIRTUAL, PROGRAMACION_13]


def testFiltrarMateriaExacta():
    assert materias.filtrarMateriaExacta(OFERTA, "álgebra i") == [ALGEBRA_02]


def testFiltrarPorComisionAceptaDistintasEscrituras():
    esperado = [PROGRAMACION_07, PROGRAMACION_07_VIRTUAL]

    assert materias.filtrarPorComision(OFERTA, "7") == esperado
    assert materias.filtrarPorComision(OFERTA, "COM-07") == esperado


def testHorariosEnAula():
    assert aulas.horariosEnAula(OFERTA, "7118", "viernes") == [PROGRAMACION_07]


def testOrdenarPorHoraNoModificaLaOriginal():
    desordenados = [PROGRAMACION_07, PROGRAMACION_13]

    assert aulas.ordenarPorHora(desordenados) == [PROGRAMACION_13, PROGRAMACION_07]
    assert desordenados == [PROGRAMACION_07, PROGRAMACION_13]


def testSeSuperponen():
    assert superposiciones.seSuperponen(PROGRAMACION_07, ALGEBRA_02)
    assert not superposiciones.seSuperponen(PROGRAMACION_13, ALGEBRA_02)
    assert not superposiciones.seSuperponen(PROGRAMACION_07_VIRTUAL, ALGEBRA_02)


def testHorariosQueSeTocanNoSeSuperponen():
    de14a18 = ["", "", "", "", "", "Lunes", "14:00", "18:00", "", "", "", "", "", ""]
    de18a22 = ["", "", "", "", "", "Lunes", "18:00", "22:00", "", "", "", "", "", ""]

    assert not superposiciones.seSuperponen(de14a18, de18a22)


def testBuscarSuperposiciones():
    pares = superposiciones.buscarSuperposiciones([PROGRAMACION_07, PROGRAMACION_07_VIRTUAL], [ALGEBRA_02])

    assert pares == [[PROGRAMACION_07, ALGEBRA_02]]
