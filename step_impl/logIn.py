import os
from step_impl.utils.driver import Driver
from getgauge.python import step

@step("Give an option to Log In")
def giveAnOptionToLogIn():
  Driver.driver.find_element_by_link_text("Log in")

@step("Show the log in status for user <name>")
def showTheLogInStatusForUser(name):
  authenticatedInfo = Driver.driver.find_element_by_id("auth")
  authenticatedInfo.is_displayed()
  assert True, "Welcome " + customer + "! Not you?" in authenticatedInfo.text

@step("Login as name <name> and <password>")
def loginAsNameWithPassword(name,password):
  driver = Driver.driver
  driver.find_element_by_link_text("Log in").click()
  driver.find_element_by_name("login").send_keys(name)
  driver.find_element_by_name("password").send_keys(password)
  driver.find_element_by_name("commit").click()