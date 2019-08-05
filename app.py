import re
import cherrypy
from bhavcopy import BhavCopy
import redis
import os
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('html'))

config = {

    'global': {
'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 5000)),
    },

    '/assets': {
        'tools.staticdir.root': os.path.dirname(os.path.abspath(__file__)),
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'assets',
    },
    '/favicon.ico': {
    'tools.staticfile.on': True,
    'tools.staticfile.filename': os.path.join(os.path.dirname(os.path.abspath(__file__)), "favicon.ico")
    }
}


class HomePage(object):
    @cherrypy.expose
    def index(self):
        output = """
            """
        tmpl = env.get_template('index.html')
        return tmpl.render(data=output)

root = HomePage()

if __name__ == '__main__':
    cherrypy.quickstart(root, "/", config=config)
