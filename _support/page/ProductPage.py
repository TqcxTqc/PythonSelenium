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
    PRODUCT_PRICE = (By.CSS_SELECTOR, "li h2")
    PRODUCT_TAX = (By.XPATH, "//li[contains(text(),'Ex Tax')]")

    # Buttons
    ADD_TO_CART = (By.CSS_SELECTOR, "#button-cart")

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

    def add_item_to_cart(self):
        button = self.browser.find_element(*ProductPage.ADD_TO_CART)
        button.click()
        assert button.text == "Loading..."

    def get_success_message(self, product_item):
        alert = self.alert.get_alert()
        assert alert.text[:-2] == f"Success: You have added {product_item} to your shopping cart!"

    def get_product_price(self, product_price, product_tax):
        actual_price = self.browser.find_element(*ProductPage.PRODUCT_PRICE)
        actual_tax = self.browser.find_element(*ProductPage.PRODUCT_TAX)
        assert actual_tax.text.split(":")[1].replace(" ", "") == product_tax
        assert actual_price.text == product_price
