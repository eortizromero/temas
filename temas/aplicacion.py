# -*- coding: latin-1 -*-

import sys
import json


# class BaseWeb(object):
#     _nombre = None
#     _foder_plantillas = None
#     _ruta_raiz = None
#
#     def __init__(self,  nombre, folder_plantillas=None, ruta_raiz=None):
#         self.nombre, self.folder_plantillas = nombre, folder_plantillas
#
#         if ruta_raiz is None:
#             print "No hay ruta Raiz"
#
#
# class Temas(BaseWeb):
#     _nombre = '/'
#
#     def __init__(self, nombre, folder_plantillas='plantillas', ruta_raiz=None):
#         BaseWeb.__init__(self, nombre, folder_plantillas=folder_plantillas, ruta_raiz=ruta_raiz)
#
#
#     def app(self, ent, iniciar_respuesta):
#         print ent['CONTENT_LENGTH']
#         datos = {
#             'Hola Mundo': 'Yes'
#         }
#         status = '200 OK'
#         cabezeras = {}
#         cabezeras['Content-Type'] = 'application/json'
#
#         if ent['CONTENT_LENGTH']:
#             peticion_cuerpo = ent['wsgi.input'].read(int(ent['CONTENT_LENGTH']))
#         cuerpo = json.dumps(datos, encoding='utf-8')
#         print cuerpo
#         cabezeras['Content-Lenght'] = str(len(cuerpo))
#         iniciar_respuesta(status, cabezeras.items())
#         return cuerpo
	
	
