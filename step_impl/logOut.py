import os
from step_impl.utils.driver import Driver
from getgauge.python import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@step("Log out the customer")
def logOutTheCustomer():
    webDriver = Driver.driver
    option = "Log out"

    try:
        element = WebDriverWait(webDriver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, option))
        )
        element.click()
    except Exception as error:
        webDriver.quit()

@step("Clear previous login")
def clear_previous_login():
    webDriver = Driver.driver
    option = "Log out"

    try:
        driver.find_element_by_link_text("Log out").click()
    except Exception as error:
        print("No previous logins")


@step("Give an option to Log Out")
def giveAnOptionToLogOut():
    webDriver = Driver.driver
    option = "Log out"

    assert True, driver.find_element_by_link_text("Log out") != null
