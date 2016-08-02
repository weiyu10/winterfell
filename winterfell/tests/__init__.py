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
        self.headers = {'X-Auth-Token': CONF.admin_token}

    def tearDown(self):
        set_config({}, overwrite=True)
