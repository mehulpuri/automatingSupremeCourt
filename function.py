from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox(executable_path="C:\Program Files (x86)\geckodriver.exe")
driver.get("https://main.sci.gov.in/case-status")
action = ActionChains(driver)
driver.maximize_window()
yearboi = 2022

def goToParty(): 
    driver.find_element("link text", "Party Name").click()

def yearInp():
   
    partyYear = Select(driver.find_element("id", "partyyear"))
    partyYear.select_by_value(str(yearboi))



def captcha():
    captcha = driver.find_element("id", "cap")
    captchaIn = driver.find_element("id", "ansCaptcha")
    action.click(on_element = captchaIn)
    action.send_keys(captcha.text[0:4])

def info():
    # element to be found
    partyName = driver.find_element("id", "partyname")
    
    #click on the element
    action.click(on_element = partyName)
    
    partyName.click()
    
    #send the key
    action.send_keys("Azim Premji")

def submit():
    driver.find_element("id", "getPartyData").click()

goToParty()
captcha()
info()
yearInp()
action.perform()
submit()


# 2nd window
driver.switch_to.new_window('tab')

driver.get("https://main.sci.gov.in/case-status")
action = ActionChains(driver)
driver.maximize_window()
yearboi = 2021

goToParty()
captcha()
info()
yearInp()
action.perform()
submit()

# 3rd window
driver.switch_to.new_window('tab')

driver.get("https://main.sci.gov.in/case-status")
action = ActionChains(driver)
driver.maximize_window()
yearboi = 2019

goToParty()
captcha()
info()
yearInp()
action.perform()
submit()

# 4th window
driver.switch_to.new_window('tab')

driver.get("https://main.sci.gov.in/case-status")
action = ActionChains(driver)
driver.maximize_window()
yearboi = 2018

goToParty()
captcha()
info()
yearInp()
action.perform()
submit()

# 5th window
driver.switch_to.new_window('tab')

driver.get("https://main.sci.gov.in/case-status")
action = ActionChains(driver)
driver.maximize_window()
yearboi = 2017

goToParty()
captcha()
info()
yearInp()
action.perform()
submit()
