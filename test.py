# -*- coding: latin-1 -*-

from temas import Temas
t = Temas(__name__)
app = t.app

if __name__ == '__main__':
	from werkzeug.serving import run_simple
	run_simple('localhost', 4000, app)
