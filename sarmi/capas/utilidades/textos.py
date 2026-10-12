from ... import configuracion


def normalizar(texto):
    """Recibe un texto.
    Lo pasa a minúsculas y le saca las tildes (ver LETRAS_CON_TILDE en configuracion.py).
    Devuelve el texto nuevo.
    Ejemplo: normalizar("Introducción a la PROGRAMACIÓN") devuelve "introduccion a la programacion"."""
    return ""


def contiene(texto, buscado):
    """Recibe dos textos: texto y buscado.
    Se fija si buscado aparece en alguna parte de texto.
    Devuelve True si aparece y False si no.
    Ejemplo: contiene("introduccion a la programacion", "program") devuelve True."""
    return False


def extraerNumero(texto):
    """Recibe un texto.
    Junta los dígitos que aparecen en el texto y los convierte en número.
    Devuelve ese número, o -1 si el texto no tiene dígitos.
    Ejemplo: extraerNumero("COM-07") devuelve 7."""
    return -1
