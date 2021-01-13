import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

dirname = os.path.dirname(__file__)


class Driver:
    def __init__(self, dirver_path=None):
        self.driver_path = dirver_path or os.path.join(dirname, "chromedriver.exe")

    def configure_driver(self):
        # add additional options to the webdriver
        chrome_options = Options()
        # add the argument and make the browser Headless.
        chrome_options.add_argument("--headless")
        # instantiate the webdriver
        self.driver = webdriver.Chrome(executable_path=self.driver_path, options=chrome_options)
        # return driver

    def get_components(self, url, expression):
        self.driver.get(url)
        # wait for the element to load
        WebDriverWait(self.driver, 5).until(expression)
        return self.driver.page_source

    def close(self):
        self.driver.close()
