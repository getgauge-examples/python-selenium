import os
from step_impl.utils.driver import Driver
from getgauge.python import step

@step("Show a message <message> <linkText>")
def showAMessage(message,linkText):
    webDriver = Driver.driver
    webDriver.find_element_by_link_text(linkText)
    flashNoticeElement = webDriver.find_element_by_xpath("//div[@id = 'flash_notice' and text() = '"+ message+"']")
    assert True,flashNoticeElement.is_displayed()
