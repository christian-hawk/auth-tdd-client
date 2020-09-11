from unittest import TestCase
import clientapp
import helper
import os
from flask import url_for
from clientapp.client_handler import ClientHandler
from unittest.mock import MagicMock, patch


class TestRegisterEndpoint(TestCase):
    def setUp(self):
        self.app = clientapp.create_app()
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        #self.oauth = OAuth(self.app)
        os.environ['AUTHLIB_INSECURE_TRANSPORT'] = "1"

    def test_if_app_has_register_endpoint(self):
        self.assertIn('register', helper.app_endpoints(clientapp.create_app()))

    def test_if_endpoint_accepts_post(self):
        methods = None
        for rule in self.app.url_map.iter_rules('register'):
            methods = rule.methods
        self.assertIn('POST', methods)

    def test_endpoint_should_return_valid_req(self):
        self.assertIn(
            self.client.post(url_for('register')).status_code, range(100, 511),
            '/configuration returned invalid requisition')

    @patch('clientapp.client_handler.ClientHandler.__init__',
           MagicMock(return_value=None))
    def test_endpoint_should_init_client_handler(self):
        self.client.post(url_for('register'))
        ClientHandler.__init__.assert_called_once()
