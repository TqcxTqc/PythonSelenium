from selenium.webdriver.common.by import By
from .BasePage import BasePage


class LoginPage(BasePage):
    CUSTOMER_TABLE = (By.CSS_SELECTOR, "div.col-sm-6:nth-child(2)")
    CUSTOMER_TABLE_TITLE = (By.CSS_SELECTOR, "div.col-sm-6:nth-child(2) h2")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#input-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value='Login']")
    FORGOT_PASSWORD = (By.CSS_SELECTOR, "div[class='form-group'] a")

    def open_login(self):
        self.top_menu.move_my_account_to_login()

    def check_page(self):
        login_table = self.browser.find_element(*LoginPage.CUSTOMER_TABLE)
        title_of_table = self.browser.find_element(*LoginPage.CUSTOMER_TABLE_TITLE)
        email = self.browser.find_element(*LoginPage.EMAIL_FIELD)
        password = self.browser.find_element(*LoginPage.PASSWORD_FIELD)
        forgot_password = self.browser.find_element(*LoginPage.FORGOT_PASSWORD)
        login_table.is_displayed()
        title_of_table.is_displayed()
        email.is_displayed()
        password.is_displayed()
        forgot_password.is_displayed()

    def click_login_button(self):
        self.browser.find_element(*LoginPage.LOGIN_BUTTON).click()

    def wait_error_alert(self):
        return self.alert.get_alert()
