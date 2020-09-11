from flask import Flask, session, redirect, request, url_for, jsonify
from authlib.integrations.flask_client import OAuth
from . import config as cfg
from logging.config import dictConfig
import logging
import base64
from flask_oidc import registration, discovery
import json
import sys
from httplib2 import RelativeURIError
from .client_handler import ClientHandler

from .ressources.errors import MismatchingStateError, OAuthError
import os

oauth = OAuth()

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s %(name)s in %(module)s : %(message)s',
    filename='test-client.log')
'''
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s %(name)s in %(module)s %(threadName)s: %(message)s',
    }},
    'handlers':
        {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
            },
        'file_handler': {
            'level': 'DEBUG',
            'filename': 'mylogfile.log',
            'class': 'logging.FileHandler',
            'formatter': 'default'

            }
        },

    'root': {
        'level': 'DEBUG',
        'handlers': ['file_handler'],
        'filename': 'demo.log'
    }

})
'''
# recebe a url do op
# descobre os dados do op com a url
# registra o cliente (app) no op com os dados do discovery
# atualiza client-id, client-secret e metadata-server

# def register_client(op_data: dict, client_url: str) -> dict:
#     """[register client and returns client information]

#     :param op_data: [description]
#     :type op_data: dict
#     :param client_url: [description]
#     :type client_url: str
#     :return: [client information including client-id and secret]
#     :rtype: dict
#     """
#     redirect_uri = '%s/oidc_callback' % client_url
#     reg_info = registration.register_client(op_data, [redirect_uri])
#     return reg_info

# def discover(op_url: str, disc:discovery=discovery) -> dict :
#     """Discover op information on .well-known/open-id-configuration
#     :param op_url: [url from OP]
#     :type op_url: str
#     :param discovery: [flask_oidc.discovery injection], defaults to discovery
#     :type discovery: discovery, optional
#     :return: [data retrieved from OP url]
#     :rtype: dict
#     """
#     op_data = {}
#     try:
#         op_data = disc.discover_OP_information(op_url)
#         print(op_data)
#         return op_data

#     except json.JSONDecodeError as err:
#         print('Error trying to decode JSON: %s' % err)

#     except RelativeURIError as err:
#         print(err)

#     except Exception as e:
#         print('An unexpected ocurred: %s' % e)

#     return op_data


def get_preselected_provider():
    provider_id_string = cfg.PRE_SELECTED_PROVIDER_ID
    print('get_preselected_provider - provider_id_string = %s' %
          provider_id_string)
    provider_object = '{ "provider" : "%s" }' % provider_id_string
    provider_object_bytes = provider_object.encode()
    base64url_bytes = base64.urlsafe_b64encode(provider_object_bytes)
    base64url_value = base64url_bytes.decode()
    print('get_preselected_provider - base64url encoded: %s' % base64url_value)
    if base64url_value.endswith('='):
        base64url_value_unpad = base64url_value.replace('=', '')
        print('get_preselected_provider - base64url encoded unpad: %s' %
              base64url_value_unpad)
        return base64url_value_unpad
    else:
        return base64url_value


def ssl_verify(ssl_verify=cfg.SSL_VERIFY):
    if ssl_verify is False:
        os.environ['CURL_CA_BUNDLE'] = ""


class BaseClientErrors(Exception):
    status_code = 500


def create_app():
    ssl_verify()

    app = Flask(__name__)

    # app.config['OIDC_CLIENT_SECRETS'] = 'client_secrets.json'

    app.secret_key = b'fasfafpj3rasdaasfglaksdgags331s'
    app.config['OP_CLIENT_ID'] = cfg.CLIENT_ID
    app.config['OP_CLIENT_SECRET'] = cfg.CLIENT_SECRET
    oauth.init_app(app)
    oauth.register('op',
                   server_metadata_url=cfg.SERVER_META_URL,
                   client_kwargs={
                       'scope': 'openid profile mail user_name',
                       'acr_value': cfg.ACR_VALUES
                   },
                   token_endpoint_auth_method='client_secret_post')

    # token_endpoint_auth_method = 'client_secret_post')
    # client_auth_methods = ['client_secret_post'])

    @app.route('/')
    def index():
        return '''
        <html>
            <head><title>Index Test</title></head>
            <body>
                <h1>Welcome to the test of your life</h1>
                <br><hr>
                <h3><a href="https://chris.testingenv.org/protected-content">
                Click here to start!</a>
            </body>
        </html>
        '''

    @app.route('/register', methods=['POST'])
    def register():
        client_handler = ClientHandler('https://t1.techno24x7.com',
                                       'https://test.com')
        content = request.json
        return {}, 100

    @app.route('/protected-content', methods=['GET'])
    def protected_content():
        app.logger.debug('/protected-content - cookies = %s' % request.cookies)
        app.logger.debug('/protected-content - session = %s' % session)
        if 'user' in session:
            return {'status': 'success'}, 200

        return redirect(url_for('login'))

    @app.route('/login')
    def login():
        app.logger.info('/login requested')
        redirect_uri = cfg.REDIRECT_URIS[0]
        app.logger.debug('/login redirect_uri = %s' % redirect_uri)
        response = oauth.op.authorize_redirect()
        query_args = {
            'redirect_uri': redirect_uri,
        }
        if cfg.PRE_SELECTED_PROVIDER is True:
            query_args[
                'preselectedExternalProvider'] = get_preselected_provider()

        if cfg.ACR_VALUES is not None:
            query_args['acr_values'] = cfg.ACR_VALUES

        response = oauth.op.authorize_redirect(**query_args)

        app.logger.debug('/login authorize_redirect(redirect_uri) url = %s' %
                         (response.location))

        return response

    @app.route('/oidc_callback')
    @app.route('/callback')
    def callback():
        try:
            if not request.args['code']:
                return 400
            app.logger.info('/callback - received %s - %s' %
                            (request.method, request.query_string))
            token = oauth.op.authorize_access_token()
            app.logger.debug('/callback - token = %s' % token)
            user = oauth.op.parse_id_token(token)
            app.logger.debug('/callback - user = %s' % user)
            session['user'] = user
            app.logger.debug('/callback - cookies = %s' % request.cookies)
            app.logger.debug('/callback - session = %s' % session)
            # TODO: get user info

            return redirect('/')

        except (MismatchingStateError, OAuthError) as error:
            print('exception!')
            print(error)
            app.logger.error(error)
            return {'error': error}, 400

    @app.route("/configuration", methods=["POST"])
    def configuration():
        '''Receives client configuration via API'''
        app.logger.info('/configuration called')
        content = request.json
        app.logger.debug("content = %s" % content)
        if content is not None:
            if 'provider_id' in content:
                cfg.PRE_SELECTED_PROVIDER_ID = content['provider_id']
                cfg.PRE_SELECTED_PROVIDER = True
                app.logger.debug('/configuration: provider_id = %s' %
                                 content['provider_id'])
                return jsonify({"provider_id": content['provider_id']}), 200

        else:
            return {}, 400

    return app
