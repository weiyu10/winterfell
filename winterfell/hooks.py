import webob
import pecan
import logging
from pecan import conf as CONF
from pecan.hooks import PecanHook
from winterfell.exception import WinterfellException

LOG = logging.getLogger(__name__)


class ExceptionHook(PecanHook):

    def on_error(self, state, exc):
        if isinstance(exc, WinterfellException):
            message = exc.message
            return webob.Response(message, status=exc.code)


class AuthHook(PecanHook):

    def before(self, state):
        request = state.request
        user_token = request.headers.get('X-Auth-Token')
        admin_token = CONF.admin_token
        if user_token == admin_token:
            LOG.info('RBAC: Bypassing authentication')
            request.is_admin = True
        else:
            pecan.abort(401, 'Authentication required')
