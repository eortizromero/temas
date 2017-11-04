# -*- coding: latin-1 -*-

from temas.controladores import controlador
from temas.ruteador import Ruteador

@controlador
def index(request):
    return "Hola Mundo"


if __name__ == '__main__':
    hola_mundo = Ruteador()
    hola_mundo.agregar_ruteo('/',  controlador=index)

    print hola_mundo
    # try:
    #     from wsgiref.simple_server import make_server
    #     httpd = make_server('localhost', 4000, app)
    #     httpd.serve_forever()
    # except KeyboardInterrupt:
    #     print "Adios"
