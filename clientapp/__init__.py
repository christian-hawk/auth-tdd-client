from flask import Flask, session, redirect
from authlib.integrations.flask_client import OAuth
from . import config as cfg





oauth = OAuth()

def create_app():
    app = Flask(__name__)
    #app.config['OIDC_CLIENT_SECRETS'] = 'client_secrets.json'
    
    app.secret_key = b'fasfafpj3rasdaasfglaksdgags331s'
    app.config['OP_CLIENT_ID'] = cfg.CLIENT_ID
    app.config['OP_CLIENT_SECRET'] = cfg.CLIENT_SECRET
    oauth.init_app(app)
    oauth.register('op',
            server_metadata_url = 'https://chris.gluuthree.org/.well-known/openid-configuration',
            client_kwargs = {
                'scope' : 'openid',
                'acr_value' : 'passport-saml'
                },
            token_endpoint_auth_method = 'client_secret_post')

    

    @app.route('/protected-content', methods=['GET'])
    def protected_content():
        if 'profile' in session:
            return {},200
        else:
            return oauth.op.authorize_redirect()

    @app.route('/login', methods=['GET'])
    def login():
        redirect_uri = cfg.REDIRECT_URIS[0]
        return oauth.op.authorize_redirect(redirect_uri)

    return app
        
if __name__ == '__main__':
    app = create_app()
    app.debug = True
    app.run(host='0.0.0.0', ssl_context=('cert.pem', 'key.pem'), port=443)





