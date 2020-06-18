CLIENT_ID = "be201b4d-dfe9-4877-8a95-5d3d64589a27"
CLIENT_SECRET = "Test123$"
CLIENT_AUTH_URI = "https://chris.gluutwo.org/oxauth/restv1/authorize"
TOKEN_URI = "https://chris.gluutwo.org/oxauth/restv1/token"
USERINFO_URI = "https://chris.gluutwo.org/oxauth/restv1/userinfo"
REDIRECT_URIS = [
    'https://chris.testingenv.org/callback'
]
ISSUER = "https://chris.gluutwo.org"

# for gluu
SAML_ACR_VALUES = "inbound-saml"
SOCIAL_ACR_VALUES = "social-saml"

# SYSTEM SETTINGS
# use with caution, unsecure requests, for develpment environments
SSL_VERIFY = False

