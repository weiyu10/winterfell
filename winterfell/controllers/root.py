from pecan import expose
from winterfell.controllers import user


class RootController(object):
    user = user.UserController()

    @expose(generic=True, template='index.html')
    def index(self):
        return dict(message='I am a mako template')
