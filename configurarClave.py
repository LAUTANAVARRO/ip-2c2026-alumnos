# Guarda la clave de Gemini en el archivo sarmi/.env
# Uso: python configurarClave.py
import os

CARPETA_DEL_PROYECTO = os.path.dirname(os.path.abspath(__file__))
RUTA_DE_LA_CLAVE = os.path.join(CARPETA_DEL_PROYECTO, "sarmi", ".env")


def armarContenido(clave):
    usarGeminiGratuito = "GOOGLE_GENAI_USE_ENTERPRISE=0\n"
    claveDeGemini = "GOOGLE_API_KEY=" + clave + "\n"

    return usarGeminiGratuito + claveDeGemini


def guardar(contenido):
    with open(RUTA_DE_LA_CLAVE, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)


def principal():
    clave = input("Pegá la clave de Gemini y apretá Enter: ")
    clave = clave.strip()

    guardar(armarContenido(clave))
    print("Listo. La clave quedó guardada en", RUTA_DE_LA_CLAVE)


if __name__ == "__main__":
    principal()
