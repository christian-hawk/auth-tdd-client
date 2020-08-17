CLIENT_ID = "6fffd04d-8cbb-4989-8e17-ece3d92ff7c5"
CLIENT_SECRET = "92f7c172-6d51-4159-98a5-58d9ead7c9e1"
CLIENT_AUTH_URI = "https://t1.techno24x7.com/oxauth/restv1/authorize"
TOKEN_URI = "https://t1.techno24x7.com/oxauth/restv1/token"
USERINFO_URI = "https://t1.techno24x7.com/oxauth/restv1/userinfo"
REDIRECT_URIS = [
    'https://chris.testingenv.org/oidc_callback'
]
ISSUER = "https://t1.techno24x7.com"

SERVER_META_URL = "https://t1.techno24x7.com/.well-known/openid-configuration"

# Token authentication method can be
# client_secret_basic
# client_secret_post
# none

SERVER_TOKEN_AUTH_METHOD = "client_secret_post"

# for gluu
ACR_VALUES = 'passport_saml'
PRE_SELECTED_PROVIDER = True
PRE_SELECTED_PROVIDER_ID = 'saml-default'

# SYSTEM SETTINGS
# use with caution, unsecure requests, for develpment environments
SSL_VERIFY = False