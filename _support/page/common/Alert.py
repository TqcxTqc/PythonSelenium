from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Alert:
    ALERT = (By.CSS_SELECTOR, "div.alert")

    def __init__(self, browser):
        self.browser = browser

    def get_danger_alert(self):
        wait = WebDriverWait(self.browser, 5)
        wait.until(EC.presence_of_element_located(Alert.ALERT))
        return self.browser.find_element(*Alert.ALERT)
