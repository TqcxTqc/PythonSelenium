import pytest
import logging
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from os import path
from datetime import datetime

LOG_FOLDER = path.abspath("logs")

logging.basicConfig(level=logging.INFO, filename=f"{LOG_FOLDER}/{datetime.now()}.log",
                    format="%(asctime)s: %(levelname)s: %(name)s: %(message)s",
                    datefmt="%m/%d/%Y %I:%M:%S %p")


class MyListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        logging.error(f"Oops..: {exception}")
        driver.save_screenshot(f"{LOG_FOLDER}/{driver.session_id}.png")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=['chrome', 'firefox', 'opera'])
    parser.addoption("--url", action="store", default="https://demo.opencart.com")
    parser.addoption("--executor", action="store", default="192.168.0.13")
    parser.addoption("--bversion", action="store", default="88.0")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--name", action="store")


@pytest.fixture()
def browser(request):
    # Collecting startup parameters for pytest
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    name = request.config.getoption("--name")
    test_name = request.node.name

    logging.info(f"==> Test {test_name} executing <==")

    executor_url = f"http://{executor}:4444/wd/hub"

    capabilities = {
        "browserName": browser,
        "browserVersion": version,
        "selenoid:options": {
            "enableVNC": vnc,
            "name": name
        }
    }

    logging.info(f"==> Initialize browser:{browser} <==")

    driver = EventFiringWebDriver(webdriver.Remote(
        command_executor=executor_url, desired_capabilities=capabilities), MyListener())

    driver.url = url

    def end():
        driver.quit()
        logging.info(f"==> Closing {browser} <==")
        logging.info(f"==> Test {test_name} finished <==")

    request.addfinalizer(end)

    return driver


@pytest.fixture()
def admin_account(request):
    request = {'username': 'demo', 'password': 'demo'}
    return request
