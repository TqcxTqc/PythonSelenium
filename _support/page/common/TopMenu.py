from selenium.webdriver.common.by import By


class TopMenu:
    MY_ACCOUNT = (By.CSS_SELECTOR, "a[title='My Account']")
    SUBMENU_LOGIN = (By.XPATH, "//a[normalize-space()='Login']")
    LOGO = (By.CSS_SELECTOR, "#logo")
    NAVIGATION_BAR = (By.XPATH, "//ul[@class='nav navbar-nav']")

    def __init__(self, browser):
        self.browser = browser

    def move_my_account_to_login(self):
        self.browser.find_element(*TopMenu.MY_ACCOUNT).click()
        self.browser.find_element(*TopMenu.SUBMENU_LOGIN).click()

    def get_top_menu_logo(self):
        return self.browser.find_element(*TopMenu.LOGO)

    def top_navigation_bar(self):
        return self.browser.find_element(*TopMenu.NAVIGATION_BAR)
