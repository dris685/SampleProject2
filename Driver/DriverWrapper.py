import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner


class DriverWrapper(unittest.TestCase):
    driver = None
    base_URL = "https://opensource-demo.orangehrmlive.com/"
    executable_path = "/Users/silviaho/PycharmProjects/SampleProject/Driver/chromedriver"

    @classmethod
    def getDriver(cls):
        return cls.driver

    @classmethod
    def setUp(cls):
        # cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver = webdriver.Safari()
        # cls.driver = webdriver.Chrome(executable_path=cls.executable_path)
        cls.driver.maximize_window()
        cls.driver.get(cls.base_URL)
        return cls.driver

    @classmethod
    def tearDown(cls):
        cls.driver.quit()
