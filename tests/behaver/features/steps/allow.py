from behave import when, then, given
import requests

@given(u'username is "{username}"')
def define_username(context, username):
    context.username = username

    
@given(u'protected content link is {protected_content}')
def define_protected_content_link(context, protected_content):
    context.protected_content = protected_content

@when(u'user clicks the protected content link')
def user_clicks_protected_content_link(context):
    context.has_clicked = True
    context.response = requests.get(context.protected_content)
    

@then(u'user access the protected content link')
def user_access_protected_content_link(context):
    assert context.response.status_code == 200
    

@given(u'user does not exist')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given user does not exist')


@then(u'user goes to external login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user goes to external login page')


@given(u'user role is "{role}"')
def define_user_role(context, role):
    context.role = role
    


@then(u'user gets a 403 error')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user gets a 403 error')


