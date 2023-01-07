CLIENT_ID = ""
CLIENT_SECRET = ""
CLIENT_AUTH_URI = "https://your-authorize-endpoint"
TOKEN_URI = "https://your-token-endpoint"
USERINFO_URI = "https://your-userinfo-endpoint"
REDIRECT_URIS = [
    'https://localhost:9090/oidc_callback'
]
ISSUER = "https://your-server's-fqdn"

SERVER_META_URL = "https://your-openid-configuration-uri"

# Token authentication method can be
# client_secret_basic
# client_secret_post
# none

SERVER_TOKEN_AUTH_METHOD = "client_secret_post"

# for gluu
ACR_VALUES = 'inbound_saml'
PRE_SELECTED_PROVIDER = False
PRE_SELECTED_PROVIDER_ID = ''
HAS_PROVIDER_HOST = False
PROVIDER_HOST_STRING = None
# PROVIDER_HOST_STRING = 'samltest.id'

# SYSTEM SETTINGS
# use with caution, unsecure requests, for develpment environments
SSL_VERIFY = True
