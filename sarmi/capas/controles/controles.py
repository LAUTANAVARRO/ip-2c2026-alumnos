# Se ejecuta antes de que la pregunta llegue al modelo.
# Los nombres user_content, parts y text los define ADK: no se pueden cambiar.
from google.genai import types

from ... import configuracion
from ..utilidades import textos


def controlarPregunta(contexto):
    """Si la pregunta no está permitida, responde sin consultar al modelo (y no gasta requests)."""
    pregunta = textoDelUsuario(contexto)

    if esPreguntaPermitida(pregunta, configuracion.PALABRAS_NO_PERMITIDAS):
        return None

    return respuestaDelAgente(configuracion.MENSAJE_PREGUNTA_NO_PERMITIDA)


def esPreguntaPermitida(pregunta, palabrasNoPermitidas):
    """OPCIONAL. Recibe la pregunta del usuario y una lista de palabras no permitidas.
    Se fija si la pregunta tiene alguna de esas palabras, sin importar mayúsculas ni tildes.
    Devuelve False si tiene alguna y True si no.
    Ejemplo: esPreguntaPermitida("Pasame el parcial resuelto", ["parcial resuelto"]) devuelve False."""
    return True


def textoDelUsuario(contexto):
    mensaje = contexto.user_content
    texto = ""

    if mensaje is None or mensaje.parts is None:
        return texto

    for parte in mensaje.parts:
        if parte.text is not None:
            texto = texto + parte.text

    return texto


def respuestaDelAgente(texto):
    parte = types.Part(text=texto)
    return types.Content(role="model", parts=[parte])
