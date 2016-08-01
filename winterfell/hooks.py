import webob
from pecan.hooks import PecanHook
from winterfell.exception import WinterfellException


class ExceptionHook(PecanHook):

    def on_error(self, state, exc):
        if isinstance(exc, WinterfellException):
            message = exc.message
            return webob.Response(message, status=exc.code)
