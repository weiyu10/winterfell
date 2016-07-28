from pecan import expose, redirect
from webob.exc import status_map
import logging


logger = logging.getLogger(__name__)

class UserController(object):
    
    @expose('json')
    def post(self, username, password='test'):
        logger.debug("create user %s" % username)
        response.status = 203
        return 'user create success'

    @expose(generic=True, template='index.html')
    def index(self):
        return dict()

    @index.when(method='POST')
    def index_post(self, q):
        redirect('https://pecan.readthedocs.io/en/latest/search.html?q=%s' % q)

    @expose('error.html')
    def error(self, status):
        try:
            status = int(status)
        except ValueError:  # pragma: no cover
            status = 500
        message = getattr(status_map.get(status), 'explanation', '')
        return dict(status=status, message=message)
