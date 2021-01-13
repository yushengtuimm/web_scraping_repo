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

    def __enter__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=self.driver_path, options=chrome_options)
        return self

    def __exit__(self, type, value, tb):
        self.driver.close()

    def get_page_source(self, url, expression):
        self.driver.get(url)
        try:
            WebDriverWait(self.driver, 5).until(expression)
        except TimeoutException:
            return None
        return self.driver.page_source
