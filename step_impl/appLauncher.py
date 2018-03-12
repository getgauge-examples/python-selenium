from getgauge.python import step
import os
from step_impl.utils.driver import Driver
@step("Go to the store website")
def gotoStoreWebsite():
  URL = os.getenv('APP_ENDPOINT')
  Driver.driver.get(URL)