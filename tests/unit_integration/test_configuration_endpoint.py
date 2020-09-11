from unittest import TestCase
import clientapp
from flask import Flask, url_for
from typing import List
import os
import json


def app_endpoints(app: Flask) -> List[str]:
    """ Return all enpoints in app """

    endpoints = []
    for item in app.url_map.iter_rules():
        endpoint = item.endpoint.replace("_", "-")
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


class TestConfigurationEndpoint(FlaskBaseTestCase):
    def test_create_app_has_configuration(self):
        self.assertTrue(
            'configuration' in app_endpoints(clientapp.create_app()),
            'endpoint /configuration does not exist in app')

    def test_configuration_endpoint_should_return_valid_req(self):
        self.assertIn(
            self.client.post(url_for('configuration')).status_code,
            range(100, 511), '/configuration returned invalid requisition')

    def test_endpoint_should_return_200_if_valid_json(self):
        headers = {'Content-type': 'application/json'}
        data = {'provider_id': 'whatever'}
        json_data = json.dumps(data)
        response = self.client.post(url_for('configuration'),
                                    data=json_data,
                                    headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_endpoint_should_return_posted_data_if_valid_json(self):
        headers = {'Content-type': 'application/json'}
        data = {'provider_id': 'whatever'}
        json_data = json.dumps(data)
        response = self.client.post(url_for('configuration'),
                                    data=json_data,
                                    headers=headers)

        self.assertEqual(json_data, json.dumps(response.json))

    def test_endpoint_should_setup_cfg_with_provider_id(self):
        headers = {'Content-type': 'application/json'}
        data = {'provider_id': 'whatever'}
        json_data = json.dumps(data)
        response = self.client.post(url_for('configuration'),
                                    data=json_data,
                                    headers=headers)

        self.assertEqual(clientapp.cfg.PRE_SELECTED_PROVIDER_ID, 'whatever')

    def test_endpoint_should_setup_cfg_with_pre_selected_provider_true(self):
        clientapp.cfg.PRE_SELECTED_PROVIDER = False
        headers = {'Content-type': 'application/json'}
        data = {'provider_id': 'whatever'}
        json_data = json.dumps(data)
        response = self.client.post(url_for('configuration'),
                                    data=json_data,
                                    headers=headers)

        self.assertTrue(clientapp.cfg.PRE_SELECTED_PROVIDER, )
