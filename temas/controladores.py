# -*- coding: latin-1 -*-

from werkzeug.wrappers import Request as Peticion, Response as Respuesta
from werkzeug.exceptions import HTTPException
import sys

def cargar_controlador(cadena):
    nombre_modulo, funcion_modulo = cadena.split(':', 1)
    __import__(nombre_modulo)
    modulo = sys.modules[nombre_modulo]
    funcion = getattr(modulo, funcion_modulo)
    return funcion


# Creamos el decorador para cada controlador
def controlador(f):
    def remplazar(entorno, iniciar_respuesta):
        peticion = Peticion(entorno)
        try:
            resp = f(peticion)
        except HTTPException, e:
            resp = e
        if isinstance(resp, basestring):
            resp = Respuesta(response=resp)
        return resp(entorno, iniciar_respuesta)
    return remplazar