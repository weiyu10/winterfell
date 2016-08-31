import os
from unittest import TestCase
from pecan import set_config
from pecan.testing import load_test_app
from pecan import conf as CONF

__all__ = ['FunctionalTest']


class FunctionalTest(TestCase):
    """
    Used for functional tests where you need to test your
    literal application and its integration with the framework.
    """

    def setUp(self):
        self.app = load_test_app(os.path.join(
            os.path.dirname(__file__),
            '../../config.py'
        ))
        self.admin_headers = {'X-Auth-Token': CONF.admin_token}

    def get_json(self, uri):
        return self.app.get(uri, headers=self.admin_headers)

    def post_json(self, uri):
        return self.app.post(uri, headers=self.admin_headers)

    def put_json(self, uri):
        return self.app.put(uri, headers=self.admin_headers)

    def delete_json(self, uri):
        return self.app.put(uri, headers=self.admin_headers)

    def tearDown(self):
        set_config({}, overwrite=True)
