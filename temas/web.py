# -*- coding: latin-1 -*-

from werkzeug.wrappers import Request as peticion, Response as respuesta


class BaseWeb(object):
	_nombre = None
	_foder_plantillas = None
	_ruta_raiz = None

	def __init__(self, nombre, folder_plantillas=None, ruta_raiz=None):
		self.nombre, self.folder_plantillas = nombre, folder_plantillas
		
		if ruta_raiz is None:
			print "No hay ruta Raiz"

class Temas(BaseWeb):
	_nombre = '/'
	
	def __init__(self, nombre, folder_plantillas='plantillas', ruta_raiz=None):
		BaseWeb.__init__(self, nombre, folder_plantillas=folder_plantillas, ruta_raiz=ruta_raiz)
		print nombre, folder_plantillas, ruta_raiz
		
	@peticion.application
	def app(self, request):
		return respuesta("Hola Mundo")
	
	
