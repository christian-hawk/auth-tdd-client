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

base_url = "https://chris.testingenv.org"

class TestAuthcomlogin():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.driver.delete_all_cookies()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_authcomlogin(self):
    # Test name: auth com login
    # Step # | name | target | value
    # 1 | open | /oxauth/login.htm | 
    self.driver.get("https://chris.gluutwo.org/oxauth/login.htm")
    # 2 | setWindowSize | 625x638 | 
    self.driver.set_window_size(625, 638)
    # 3 | click | id=username | 
    self.driver.find_element(By.ID, "username").click()
    # 4 | click | id=username | 
    self.driver.find_element(By.ID, "username").click()
    # 5 | doubleClick | id=username | 
    element = self.driver.find_element(By.ID, "username")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    # 6 | type | id=username | johndoo
    self.driver.find_element(By.ID, "username").send_keys("johndoo")
    # 7 | type | id=password | test123
    self.driver.find_element(By.ID, "password").send_keys("test123")
    # 8 | click | id=loginButton | 
    self.driver.find_element(By.ID, "loginButton").click()