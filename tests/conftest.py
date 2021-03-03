import pytest
from selenium import webdriver
from os import path

DRIVER_PATH = path.abspath("drivers")


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     choices=['chrome', 'firefox', 'opera']
                     )
    parser.addoption("--url",
                     action="store",
                     default="https://demo.opencart.com"
                     )
    parser.addoption("--drivers",
                     action="store",
                     default=DRIVER_PATH
                     )
    parser.addoption("--headless",
                     action="store_true",
                     help="Run browser as Headless"
                     )


def get_browser_driver(drivers, browser, headless):
    """Selecting driver from executable path,parameter and browser name"""
    if browser == "chrome":
        if headless:
            option = webdriver.ChromeOptions()
            option.headless = True
            return webdriver.Chrome(executable_path=path.join(drivers, "chromedriver"), options=option)
        return webdriver.Chrome(executable_path=path.join(drivers, "chromedriver"))
    elif browser == "firefox":
        if headless:
            option = webdriver.FirefoxOptions()
            option.headless = True
            return webdriver.Firefox(executable_path=path.join(drivers, "geckodriver"), options=option)
        return webdriver.Firefox(executable_path=path.join(drivers, "geckodriver"))
    elif browser == "opera":
        return webdriver.Opera(executable_path=path.join(drivers, "operadriver"))
    else:
        return f"{browser} not found"


@pytest.fixture()
def browser(request):
    # Collecting startup parameters for pytest
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    drivers = request.config.getoption("--drivers")

    driver = get_browser_driver(drivers, browser, headless)
    driver.url = url
    driver.maximize_window()
    request.addfinalizer(driver.quit)

    return driver


@pytest.fixture()
def admin_account(request):
    request = {'username': 'demo', 'password': 'demo'}
    return request
