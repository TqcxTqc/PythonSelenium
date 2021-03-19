import logging
from .common.TopMenu import TopMenu
from .common.Alert import Alert
from .common.Footer import Footer


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.top_menu = TopMenu(self.browser)
        self.alert = Alert(self.browser)
        self.footer = Footer(self.browser)
        self.logger = logging.getLogger(type(self).__name__)

    def open_special_page(self, url):
        self.logger.info(f"Opening {self.browser.url}{url}")
        self.browser.get(f"{self.browser.url}{url}")

    def check_page_element_is_present(self, *args):
        """Find an element given a By strategy and locator"""
        self.logger.info(f"Searching element {args}")
        label = self.browser.find_element(*args)
        label.is_displayed()

    def open_page(self):
        self.logger.info(f"Opening page {self.browser.url}")
        self.browser.get(self.browser.url)
