
# Test-Auth-Client

Little change

This client aims to be a reliable sclient build with BDD / TDD metologies to be used in auth testing.

Flask based auth/identity app based on test-first, made to encourage and learn BDD and TDD.


## Authorization code flow / Protected Ressources

![auth code flow](docs/images/authorize_code_flow.png)

``` websequencediagrams.com
actor User
User->Browser: Clicks login
Browser->App:
App->OP: authorization code request
OP->Browser: Redirect to login prompt
User->Browser: Authenticate and Conset
Browser->OP:Post Ahthenticate and consent
User->OP: Authenticate and consent
OP->App: Returns authorization code
App->OP: Request access/id token
OP->OP: Validates authorization code
OP->App: Returns ID Token / Access Token
App->App: Create a new session\n with same state
App->Browser: Set session cookies, \nRedirects to protected resource
Browser->App: Request protected ressource
App->App: Restore previous token from DB
App->App: Validate session / token
App->App: Return protected-content\nOr unauthorized error
```

## Developing

### Test First

- BDD black box: independent testing using behave and selenium
- TDD: Test first, always: unit tests using unittest lib and pytest
- Coverage: minimum accepted: 80%



