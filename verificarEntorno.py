# Revisa que la compu tenga todo lo necesario para hacer el TP.
# Uso: python verificarEntorno.py
# La última prueba le manda un mensaje a Gemini: usa 1 request de la clave.
import os
import sys

VERSION_MINIMA_DE_PYTHON = (3, 10)
CARPETA_DEL_PROYECTO = os.path.dirname(os.path.abspath(__file__))
RUTA_DE_LA_CLAVE = os.path.join(CARPETA_DEL_PROYECTO, "sarmi", ".env")
PREGUNTA_DE_PRUEBA = "Respondé solamente: OK"


def informar(descripcion, salioBien):
    if salioBien:
        print("[OK]    " + descripcion)
    else:
        print("[FALLA] " + descripcion)


def tienePythonActualizado():
    return sys.version_info >= VERSION_MINIMA_DE_PYTHON


def tieneAdkInstalado():
    try:
        import google.adk
        return True
    except ImportError:
        return False


def leerClave():
    from dotenv import dotenv_values

    if not os.path.exists(RUTA_DE_LA_CLAVE):
        return ""

    valores = dotenv_values(RUTA_DE_LA_CLAVE)
    return valores.get("GOOGLE_API_KEY", "")


def conectaConGemini(clave):
    from google import genai
    from sarmi import configuracion

    try:
        cliente = genai.Client(api_key=clave)
        cliente.models.generate_content(model=configuracion.MODELO, contents=PREGUNTA_DE_PRUEBA)
        return True
    except Exception as error:
        print("        " + str(error))
        return False


def principal():
    version = str(sys.version_info[0]) + "." + str(sys.version_info[1])
    informar("Python 3.10 o superior (instalado: " + version + ")", tienePythonActualizado())

    adkInstalado = tieneAdkInstalado()
    informar("Paquetes instalados (google-adk)", adkInstalado)
    if not adkInstalado:
        print("        Activá el entorno virtual y corré: pip install -r requirements.txt")
        return

    clave = leerClave()
    informar("Clave de Gemini guardada", clave != "")
    if clave == "":
        print("        Guardala con: python configurarClave.py")
        return

    informar("Conexión con Gemini (" + PREGUNTA_DE_PRUEBA + ")", conectaConGemini(clave))


if __name__ == "__main__":
    principal()
