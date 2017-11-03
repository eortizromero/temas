# -*- coding: latin-1 -*-

from temas import Temas
t = Temas(__name__)
app = t.app

if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server
        httpd = make_server('localhost', 4000, app)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print "Adios"
