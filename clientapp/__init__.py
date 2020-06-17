from flask import Flask, session, redirect, request, url_for
from authlib.integrations.flask_client import OAuth
from . import config as cfg
from logging.config import dictConfig
from ressources.errors import MismatchingStateError, OAuthError
import os

#test
oauth = OAuth()

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


def ssl_verify(ssl_verify = cfg.SSL_VERIFY):
    if ssl_verify == False:
        os.environ['CURL_CA_BUNDLE'] = ""
        


class BaseClientErrors(Exception):
    status_code = 500



def create_app():
    ssl_verify()

    app = Flask(__name__)
    

    #app.config['OIDC_CLIENT_SECRETS'] = 'client_secrets.json'
    
    app.secret_key = b'fasfafpj3rasdaasfglaksdgags331s'
    app.config['OP_CLIENT_ID'] = cfg.CLIENT_ID
    app.config['OP_CLIENT_SECRET'] = cfg.CLIENT_SECRET
    oauth.init_app(app)
    oauth.register('op',
            server_metadata_url = 'https://chris.gluutwo.org/.well-known/openid-configuration',
            client_kwargs = {
                'scope' : 'openid profile email',
                'acr_value' : 'passport-saml'
                })
            
            #token_endpoint_auth_method = 'client_secret_post')
            #client_auth_methods = ['client_secret_post'])

    @app.route('/')
    def index():
        #return "<html><header><title>testando</title></header><body><h1>Teste</h1></body></html>",200
        return '''
        <html>
            <head><title>Index Test</title></head>
            <body>
                <h1>Welcome to the test of your life</h1>
                <br><hr>
                <h3><a href="https://chris.testingenv.org/protected-content">Click here to start!</a>
            </body>
        </html>
        '''

    @app.route('/protected-content', methods=['GET'])
    def protected_content():
        app.logger.debug('TESTING DEBUG LEVEL')
        
        if 'user' in session:
            
            return {'status':'success'},200
        else:
            #return redirect("https://chris.testingenv.org/login")
            return redirect(url_for('login', _external=True))

    @app.route('/login')
    def login():
        app.logger.info('/login requested')
        redirect_uri = cfg.REDIRECT_URIS[0]
        app.logger.debug('/login redirect_uri = %s' % redirect_uri)
        response = oauth.op.authorize_redirect(redirect_uri)
        app.logger.debug('/login authorize_redirect(redirect_uri) url = %s' % response.location)
        return response
        
    

    @app.route('/callback')
    def callback():
        try:    
            if not request.args['code']:
                return 400
            app.logger.info('/callback - received %s - %s' % (request.method, request.query_string))
            token = oauth.op.authorize_access_token()
            app.logger.debug('/callback - token = %s' % token)
            user = oauth.op.parse_id_token(token)
            app.logger.debug('/callback - user = %s' % user)
            session['user'] = user
            app.logger.debug('/callback - cookies = %s' % request.cookies)
            app.logger.debug('/callback - session = %s' % session)
            
            #get user info


            return redirect('/')

        except (MismatchingStateError, OAuthError) as error:
            print('exception!')
            app.logger.error(error)
            return {},400

    return app


'''       
if __name__ == '__main__':
    app = create_app()
    app.debug = True
    app.run(host='0.0.0.0', ssl_context=('cert.pem', 'key.pem'), port=443)
'''
