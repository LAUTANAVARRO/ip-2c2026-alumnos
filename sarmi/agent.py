from google.adk.agents import Agent

from . import configuracion
from .capas.controles import controles
from .capas.herramientas import herramientas

# ADK busca una variable llamada root_agent: ese nombre no se puede cambiar.
root_agent = Agent(
    name=configuracion.NOMBRE_DEL_AGENTE,
    model=configuracion.MODELO,
    description=configuracion.DESCRIPCION_DEL_AGENTE,
    instruction=configuracion.INSTRUCCIONES_DEL_AGENTE,
    before_agent_callback=controles.controlarPregunta,
    tools=[
        herramientas.consultarMateria,
        herramientas.consultarAula,
        herramientas.consultarSuperposicion,
        herramientas.consultarTurno,
    ],
)
