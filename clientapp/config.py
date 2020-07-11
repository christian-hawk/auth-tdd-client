CLIENT_ID = "f533946c-3e1c-4e9e-90db-c662e89a7ad3"
CLIENT_SECRET = "0c5da951-22bf-47dc-8db7-000e829d5f3f"
CLIENT_AUTH_URI = "https://chris.gluuthree.org/oxauth/restv1/authorize"
TOKEN_URI = "https://chris.gluuthree.org/oxauth/restv1/token"
USERINFO_URI = "https://chris.gluuthree.org/oxauth/restv1/userinfo"
REDIRECT_URIS = [
    'https://chris.testingenv.org/oidc_callback'
]
ISSUER = "https://chris.gluuthree.org"

SERVER_META_URL = "https://chris.gluuthree.org/.well-known/openid-configuration"

# Token authentication method can be
# client_secret_basic
# client_secret_post
# none

SERVER_TOKEN_AUTH_METHOD = "client_secret_post"

# for gluu
ACR_VALUES = ''
SAML_ACR_VALUES = "inbound_saml"
SOCIAL_ACR_VALUES = "passport_social"
PRE_SELECTED_PROVIDER = False
PRE_SELECTED_PROVIDER_ID = 'saml-emaillink'

# SYSTEM SETTINGS
# use with caution, unsecure requests, for develpment environments
SSL_VERIFY = False