from unittest import TestCase
import clientapp
from flask import Flask, url_for
from typing import List
import os

def app_endpoints(app: Flask) -> List[str]:
    """ Return all enpoints in app """
    
    endpoints = []
    for item in app.url_map.iter_rules():
        endpoint = item.endpoint.replace("_","-")
        endpoints.append(endpoint)
    return endpoints

class FlaskBaseTestCase(TestCase):
    def setUp(self):
        self.app = clientapp.create_app()
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        #self.oauth = OAuth(self.app)
        os.environ['AUTHLIB_INSECURE_TRANSPORT'] = "1"

class TestLoginEndpoint(FlaskBaseTestCase):
    def test_login_endpoint_should_exist(self):
        endpoints = app_endpoints(clientapp.create_app())
        self.assertTrue(
            'login' in app_endpoints(clientapp.create_app()),
            'endpoint /login does not exist in app'
        )


    def test_endpoint_should_return_status_code_302(self):
        self.assertEqual(
            self.client.get(url_for('login')).status_code,
            302,
            'Login endpoint is not returning 302 status_code'
        )

    def test_login_endpoint_shoud_return_a_redirection_url(self):
        self.assertIsNotNone(
            self.client.get(url_for('login')).location,
            'login endpoint does not have a redirection url'
        )

    def test_login_redirect_should_start_with_config_authorization_endpoint(self):
        self.assertTrue(
            self.client.get(url_for('login')).location.startswith(
                clientapp.cfg.CLIENT_AUTH_URI
            ),
            'Login endpoint does not redirect to cfg.CLIENT_AUTH_URI'
        )

    def test_login_endpoint_should_redirect_to_oauth_authorize_redirect_met(self):
        authorize_redirect_response = clientapp.oauth.op.authorize_redirect(
            clientapp.cfg.REDIRECT_URIS[0]
        ).location.split('state')[0]

        endpoint_response_red_url = self.client.get(url_for(
            'login')).location.split('state')[0]

        self.assertEqual(
            authorize_redirect_response,
            endpoint_response_red_url,
            'Endpoint redireciona para um endpoint diferente do metodo \
            authorize_redirect'
        )
    
    def test_login_endpoint_should_redirect_to_metadata_authorization_endpoint(self):

        response = self.client.get(url_for('login'))
        
        self.assertTrue(
            response.location.startswith(
                clientapp.oauth.op.server_metadata['authorization_endpoint']
            )

        )
    
    
   