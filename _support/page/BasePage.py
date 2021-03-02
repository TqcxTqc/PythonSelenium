from .common.TopMenu import TopMenu
from .common.Alert import Alert


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.top_menu = TopMenu(self.browser)
        self.alert = Alert(self.browser)

    def open_special_page(self, url):
        self.browser.get(f"{self.browser.url}{url}")

    def check_page_element_is_present(self, *args):
        """Find an element given a By strategy and locator"""
        label = self.browser.find_element(*args)
        label.is_displayed()

    def open_page(self):
        self.browser.get(self.browser.url)
