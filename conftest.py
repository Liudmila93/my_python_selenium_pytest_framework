import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def open_browser(request):
    browser_name = request.config.getoption("--browser")
    environment = request.config.getoption("--env")
    print(f"Creating {browser_name} driver")
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-cache")
    options.add_argument("--disable-cookies")
    if browser_name == "chrome":
        my_driver = webdriver.Chrome()
        my_driver.maximize_window()
    elif browser_name == "firefox":
        my_driver = webdriver.Firefox()
        my_driver.maximize_window()
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox' but get {browser_name}")
    my_driver.get(f"https://www.{environment}beerwulf.com/en-nl/my-account/Login?ReturnUrl=/en-NL/AccountInformation/OrderHistory")
    yield my_driver
    print(f"Closing {browser_name} driver")
    my_driver.quit()


def pytest_addoption(parser):
    """Configure custom command line parameters"""
    parser.addoption("--browser", action="store", default="chrome", help="choose browser to execute test")
    parser.addoption("--env", action="store", default="", help="choose environment to execute test. stage.")  #  test, stage, prod