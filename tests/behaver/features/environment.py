from selenium import webdriver
import os

def before_all(context):
    os.environ['CURL_CA_BUNDLE'] = ""
    
    

def before_scenario(context,scenario):
    context.web = webdriver.Firefox()

def after_scenario(context,scenario):
    context.web.delete_all_cookies()
    context.web.close()
    



def after_step(context,step):
    print()

def after_all(context):
    pass
