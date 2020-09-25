CLIENT_ID = "a7e1125da-b164-4aa9-85e9-456f510c7eda"
CLIENT_SECRET = "a911acfa2-c4e2-4258-987c-af47864be058"
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
PRE_SELECTED_PROVIDER_ID = ''

# SYSTEM SETTINGS
# use with caution, unsecure requests, for develpment environments
SSL_VERIFY = False
