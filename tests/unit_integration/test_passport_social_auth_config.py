from unittest import TestCase
import clientapp
# from flask import Flask
import os
import json


# mock client configuration
class TestPassportBase(TestCase):

    def setUp(self):

        with open('config/passport_social_test.json') as json_test_file:
            self.json_cfg = json.load(json_test_file)['web']
        
        # import ipdb; ipdb.set_trace()
        self.app = clientapp.create_app()
        self.oauth = clientapp.oauth
        self.app.config['PSOCIAL_CLIENT_ID'] = self.json_cfg['client_id']
        self.app.config['PSOCIAL_CLIENT_SECRET'] = self.json_cfg['client_secret']
        self.app.testing = True
        self.app_context = self.app.test_request_context(
            base_url="https://chris.testingenv.org")

        self.app_context.push()
        self.client = self.app.test_client()

        # registering w/ passport params
        
        self.oauth.register(
            'psocial',
            overwrite=True,
            client_secret=self.json_cfg['client_id'],
            client_id=self.json_cfg['client_secret'],
            server_metadata_url=self.json_cfg['metadata-provider'],
            authorize_params=clientapp.cfg.SOCIAL_ACR_VALUES,
            client_kwargs={
                'scope': 'openid profile email'
                }
        )
        clientapp.oauth.op = self.oauth.psocial
        os.environ['AUTHLIB_INSECURE_TRANSPORT'] = "1"


class TestSocialAuthConfig(TestPassportBase):
    
    # Config file should have passport_social
    def test_if_metadata_url_is_same_from_json_config(self):
        # import ipdb; ipdb.set_trace()
        
        self.assertEqual(
            clientapp.oauth.op._server_metadata_url,
            self.json_cfg['metadata-provider']
        )
    
    # def test_if_

    # if acr_values=passport_social
