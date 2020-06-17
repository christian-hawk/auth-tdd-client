from behave import when, then, given
import requests
from clientapp import create_app
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities




def setup_method():
    self.driver = webdriver.Firefox()
    self.vars = {}

setup_method()

def teardown_method():
    self.driver.quit()

@given(u'username is "{username}"')
def define_username(context, username):
    context.username = username
    context.password = "test123"

@given(u'user is authenticated')
def user_authenticates(context):
    self.driver.get("https://chris.testingenv.org/login")
    self.driver.set_window_size(625, 638)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("johndoo")
    self.driver.find_element(By.ID, "password").send_keys("test123")
    self.driver.find_element(By.ID, "loginButton").click()
    
@given(u'protected content link is {protected_content}')
def define_protected_content_link(context, protected_content):
    context.protected_content = protected_content

@when(u'user clicks the protected content link')
def user_clicks_protected_content_link(context):
    self.driver.get(base_url)
    self.ddriver.find_element_by_xpath(
        '//a[@href="https://chris.testingenv.org/protected-content"]'
        ).click()
    context.has_clicked = True
    context.response = requests.get(context.protected_content)
    #import ipdb; ipdb.set_trace()
    

@then(u'user access the protected content link')
def user_access_protected_content_link(context):
    import ipdb; ipdb.set_trace()
    
    assert (context.response.status_code == (200 or 302))
    

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

teardown_method()
