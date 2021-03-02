from _support.page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    # URL
    SAMSUNG_GALAXY_ITEM = "/index.php?route=product/product&path=57&product_id=49"

    # Locators
    TITLE = (By.CSS_SELECTOR, "div[id='content'] h1")
    PRODUCT_CODE = (By.XPATH, "//li[contains(text(),'Product Code:')]")
    REWARD_POINT = (By.XPATH, "//li[contains(text(),'Reward Points:')]")
    AVAILABILITY = (By.XPATH, "//li[contains(text(),'Availability:')]")

    def check_product_title(self, title):
        assert self.browser.find_element(*ProductPage.TITLE).text == title

    def check_product_info_data(self, *args):
        """Provide data after ':' sign for checking"""
        expected_data = list(args)
        actual_data = []

        for product in self.__get_products_info():
            actual_data.append(product.split(":")[1].replace(" ", ""))

        for item in range(len(expected_data)):
            assert expected_data[item] == actual_data[item]

    def __get_products_info(self):
        locators = [ProductPage.PRODUCT_CODE, ProductPage.REWARD_POINT, ProductPage.AVAILABILITY]
        result = []
        for item in range(len(locators)):
            result.append(self.browser.find_element(*locators[item]).text)
        return result
