from selenium.webdriver.common.by import By


class Footer:
    FOOTER = (By.CSS_SELECTOR, "footer .col-sm-3")
    FOOTER_TITLE = (By.CSS_SELECTOR, "footer .col-sm-3 h5")

    def __init__(self, browser):
        self.browser = browser

    def get_footer(self):
        return self.browser.find_elements(*Footer.FOOTER)
