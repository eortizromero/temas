# -*- coding: latin-1 -*-

from werkzeug.wrappers import Request as Peticion, Response as Respuesta
from werkzeug.exceptions import NotFound
from controladores import cargar_controlador
import re

# variable con validacion de expresion regular con estructura  TODO {nombre:expresion regular}
var_expreg = re.compile(r''' \{ (\w+)  (?::([^}]+))?\}  ''', re.VERBOSE)

def plantilla_para_expreg(plantilla):
    expreg = ''
    ultima_pos = 0
    for m in var_expreg.finditer(plantilla):
        expreg += re.escape(plantilla[ultima_pos:m.start()])
        var_n = m.group(1)
        expr = m.group(2) or '[^/]+'
        expr = '(?P<%s>%s)' % (var_n, expr)
        expreg += expr
        ultima_pos = m.end()

    expreg += re.escape(plantilla[ultima_pos:])
    expreg = '^%s$' % expreg
    return  expreg


class Ruteador(object):
    def __init__(self):
        self.ruteadores = []

    def agregar_ruteo(self, plantilla, controlador, **vars):
        if isinstance(controlador, basestring):
            controlador = cargar_controlador(controlador)
        self.ruteadores.append((re.compile(plantilla_para_expreg(plantilla)), controlador, vars))

    def __call__(self, entorno, iniciar_respuesta):
        peticion = Peticion(entorno)
        for expreg, controlador, vars in self.ruteadores:
            m = expreg.match(peticion.path)
            if m:
                peticion.url_vars = m.groupdict()
                peticion.url_vars.update(vars)
                return controlador(entorno, iniciar_respuesta)
        return NotFound() (entorno, iniciar_respuesta)
