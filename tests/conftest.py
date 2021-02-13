import pytest
from selenium import webdriver
from os import path

DRIVER_PATH = path.abspath("../drivers/")


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     choices=['chrome', 'firefox', 'opera']
                     )
    parser.addoption("--url",
                     action="store",
                     default="https://demo.opencart.com/"
                     )
    parser.addoption("--drivers",
                     action="store",
                     default=DRIVER_PATH
                     )


def get_driver(drivers, browser):
    """Selecting driver from executable path and browser name"""
    if browser == "chrome":
        return webdriver.Chrome(executable_path=path.join(drivers, "chromedriver.exe"))
    elif browser == "firefox":
        return webdriver.Firefox(executable_path=path.join(drivers, "geckodriver.exe"))
    elif browser == "opera":
        return webdriver.Opera(executable_path=path.join(drivers, "operadriver.exe"))
    else:
        return f"{browser} not found"


@pytest.fixture()
def browser(request):
    # Collecting startup parameters for pytest
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")

    driver = get_driver(drivers, browser)

    driver.url = url
    driver.get(url)

    driver.maximize_window()

    request.addfinalizer(driver.close)

    return driver
