from selenium.webdriver.common.by import By


class TopMenu:
    MY_ACCOUNT = (By.CSS_SELECTOR, "a[title='My Account']")
    SUBMENU_LOGIN = (By.XPATH, "//a[normalize-space()='Login']")

    def __init__(self, browser):
        self.browser = browser

    def move_my_account_to_login(self):
        self.browser.find_element(*TopMenu.MY_ACCOUNT).click()
        self.browser.find_element(*TopMenu.SUBMENU_LOGIN).click()
        page_title = self.browser.title
        assert page_title == "Account Login"
