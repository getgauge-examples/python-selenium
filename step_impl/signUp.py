import os
from step_impl.utils.driver import Driver
from getgauge.python import step

@step("Sign up as <customer> with email <email> and <password>")
def signupAs(customer,email,password):
    webDriver = Driver.driver
    webDriver.find_element_by_link_text("Sign up").click()
    form = webDriver.find_element_by_id("new_user")
    form.find_element_by_name("user[username]").send_keys(customer)
    form.find_element_by_name("user[email]").send_keys(email)
    form.find_element_by_name("user[password]").send_keys(password)
    form.find_element_by_name("user[password_confirmation]").send_keys(password)
    form.find_element_by_name("commit").click()

@step("See items available for purchase.")
def seeItemsAvailableForPurchase():
    webDriver = Driver.driver
    products = webDriver.find_elements_by_class_name("product")
    assert True, len(products)!= 0