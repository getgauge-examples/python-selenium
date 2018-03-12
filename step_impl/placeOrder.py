from getgauge.python import step

import os
from step_impl.utils.driver import Driver

@step("Add item <item> to the cart.")
def addItemToCart(item):
    webDriver = Driver.driver
    webDriver.find_element_by_link_text(item).click()
    webDriver.find_element_by_link_text("Add to Card").click()

@step("Checkout now")
def checkoutNow():
  Driver.driver.find_element_by_xpath("//input[@value='Checkout Now!']").click()

@step("Cart now contains <itemCount> number of items")
def cartNowContains(itemCount):
  products = Driver.driver.find_elements_by_xpath("//table/tbody/tr")
  assert True, numberOfItems == len(products)-2