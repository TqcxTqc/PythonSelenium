from selenium.webdriver.common.by import By


class AdminPage:
    ADMIN_URL = "/admin"
    LABEL_USERNAME = (By.CSS_SELECTOR, "label[for='input-username']")
    LABEL_PASSWORD = (By.CSS_SELECTOR, "label[for='input-password']")
    USERNAME_FIELD = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ADMIN_TITLE = (By.CSS_SELECTOR, ".container-fluid h1")
    ORDERS_ITEM_COUNT = (By.XPATH, "//div[@class='col-sm-6 text-right']")
    __NAVIGATION_SALES = (By.XPATH, "//a[contains(text(),'Sales')]")
    __SALES_SUBMENU_ORDERS = (By.XPATH, "//a[contains(text(),'Orders')]")

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(f"{self.driver.url}{AdminPage.ADMIN_URL}")

    def check_page_label_is_present(self, *args):
        """Find an element given a By strategy and locator"""
        browser = self.driver
        label = browser.find_element(*args)
        label.is_displayed()

    def sign_in_admin_panel(self, username, password):
        browser = self.driver
        username_field = browser.find_element(*AdminPage.USERNAME_FIELD)
        password_field = browser.find_element(*AdminPage.PASSWORD_FIELD)
        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)
        browser.find_element(*AdminPage.LOGIN_BUTTON).click()

    def navigate_to_ordes_in_sales(self):
        browser = self.driver
        browser.find_element(*AdminPage.__NAVIGATION_SALES).click()
        browser.find_element(*AdminPage.__SALES_SUBMENU_ORDERS).click()

    def get_title_page(self):
        browser = self.driver
        title_text = browser.find_element(*AdminPage.ADMIN_TITLE)
        return title_text.text

    def get_order_items_count(self):
        browser = self.driver
        order_count = browser.find_element(*AdminPage.ORDERS_ITEM_COUNT)
        return order_count.text[:-12]
