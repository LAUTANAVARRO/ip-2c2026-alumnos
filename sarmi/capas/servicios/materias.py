from ... import configuracion
from ..utilidades import listas, textos


def valoresDistintos(horarios, posicion):
    """Recibe una lista de horarios y una posición (ver POSICION_... en configuracion.py).
    Junta el dato que está en esa posición en cada horario, sin repetir.
    Devuelve la lista de esos valores, en el orden en que aparecen.
    Ejemplo: con los horarios de Introducción a la Programación y POSICION_COMISION,
    devuelve ["COM-01", "COM-02", "COM-03", ...]."""
    return []


def buscarMateria(oferta, nombre):
    """Recibe la oferta y el nombre de una materia, o una parte (por ejemplo "programacion").
    Busca los horarios cuya materia contiene ese nombre, sin importar mayúsculas ni tildes.
    Devuelve la lista de esos horarios, o una lista vacía si no hay ninguno.
    Ejemplo: buscarMateria(oferta, "programacion") devuelve los horarios de Introducción a la
    Programación, Programación I, Programación II y otras."""
    return []


def filtrarMateriaExacta(horarios, nombre):
    """Recibe una lista de horarios y el nombre de una materia.
    Se queda con los horarios cuya materia se llama exactamente así, sin importar mayúsculas ni tildes.
    Devuelve la lista de esos horarios, o una lista vacía si no hay ninguno.
    Ejemplo: si están los horarios de Programación I y de Programación II, con "programación i"
    devuelve solo los de Programación I."""
    return []


def filtrarPorComision(horarios, comision):
    """Recibe una lista de horarios y una comisión, escrita como sea ("7", "07", "COM-07" o "comisión 7").
    Se queda con los horarios de esa comisión, comparando solo el número.
    Devuelve la lista de esos horarios, o una lista vacía si no hay ninguno.
    Ejemplo: con los horarios de Introducción a la Programación y "7", devuelve los dos horarios
    de la COM-07: el del viernes y el virtual."""
    return []
