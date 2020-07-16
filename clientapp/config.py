CLIENT_ID = "c5993da4-0627-43f4-9fd3-6d9ef9cf63f8"
CLIENT_SECRET = "e72a4406-6f54-404c-85f9-3c72c90f870d"
CLIENT_AUTH_URI = "https://chris.gluuthree.org/oxauth/restv1/authorize"
TOKEN_URI = "https://chris.gluuthree.org/oxauth/restv1/token"
USERINFO_URI = "https://chris.gluuthree.org/oxauth/restv1/userinfo"
REDIRECT_URIS = ['https://chris.testingenv.org/oidc_callback']
ISSUER = "https://chris.gluuthree.org"

SERVER_META_URL = "https://chris.gluuthree.org/.well-known/openid-configuration"

# Token authentication method can be
# client_secret_basic
# client_secret_post
# none

SERVER_TOKEN_AUTH_METHOD = "client_secret_post"

# for gluu
ACR_VALUES = ''
PRE_SELECTED_PROVIDER = False
PRE_SELECTED_PROVIDER_ID = ''

# SYSTEM SETTINGS
# use with caution, unsecure requests, for develpment environments
SSL_VERIFY = False
