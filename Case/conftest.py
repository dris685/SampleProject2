import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome", "firefox", "safari"], scope='class')
def init_driver(request):
    global driver
    base_URL = "https://opensource-demo.orangehrmlive.com/"
    if request.param == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif request.param == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif request.param == "safari":
        driver = webdriver.Safari()
    driver.delete_all_cookies()
    driver.maximize_window()
    if isinstance(base_URL, str):
        driver.get(base_URL)
    else:
        raise TypeError("URL must be a string")
    request.cls.driver = driver
    # else:
    #     print("Your browser name: " + request.cls.driver + " is incorrect")
    #     raise Exception("driver is undefined")
    yield
    driver.quit()
