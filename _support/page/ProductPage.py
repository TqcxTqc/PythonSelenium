from _support.page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    # URL
    SAMSUNG_GALAXY_ITEM = "/index.php?route=product/product&path=57&product_id=49"
    CATALOGUE_URL = "/index.php?route=product/category&path=20"

    # Locators
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div[id='content'] h1")
    PRODUCT_CODE = (By.XPATH, "//li[contains(text(),'Product Code:')]")
    REWARD_POINT = (By.XPATH, "//li[contains(text(),'Reward Points:')]")
    AVAILABILITY = (By.XPATH, "//li[contains(text(),'Availability:')]")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "li h2")
    PRODUCT_TAX = (By.XPATH, "//li[contains(text(),'Ex Tax')]")
    TITLE_PRODUCTS_ON_PAGE = (By.CSS_SELECTOR, ".caption a")
    LEFT_MENU = (By.CSS_SELECTOR, "#column-left")
    COMPARE_BUTTON = "(//div[@class='button-group']/button[contains(@onclick,'compare.add')])"
    COMPARE_LINK = (By.CSS_SELECTOR, "#compare-total")

    # Buttons
    ADD_TO_CART = (By.CSS_SELECTOR, "#button-cart")

    def check_product_title(self, title):
        assert self.browser.find_element(*ProductPage.PRODUCT_TITLE).text == title

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

    def get_all_items_title_on_page(self, expected_items):
        get_items_title = self.browser.find_elements(*ProductPage.TITLE_PRODUCTS_ON_PAGE)
        item_titles = []
        for item in get_items_title:
            item_titles.append(item.text)

        assert item_titles == expected_items

    def select_item_in_left_menu(self, value):
        """Enter value as named on left menu"""
        try:
            select_item = {"PC": 2,
                           "Mac": 3,
                           "Laptops & Notebooks": 4,
                           "Components": 5,
                           "Tablets": 6,
                           "Software": 7,
                           "Phone & PDAs": 8,
                           "Cameras": 9,
                           "MP3 Players": 10
                           }
            left_menu = self.browser.find_element(*ProductPage.LEFT_MENU)
            selected_item = left_menu.find_element_by_css_selector(f".list-group-item:nth-child({select_item[value]})")
            selected_item.click()
        except KeyError:
            return f"No such {value} in the list"

    def check_item_to_be_present(self, item):
        wait = WebDriverWait(self.browser, 5)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".caption h4"), f"{item}"))

    def click_comparison_button(self, number):
        wait = WebDriverWait(self.browser, 5)
        wait.until(EC.element_to_be_clickable((By.XPATH, f"{ProductPage.COMPARE_BUTTON}[{number}]"))).click()
        self.alert.get_alert()

    def check_compare_link(self, item_count):
        """Checking Product Compare (number) link"""
        compare_link = self.browser.find_element(*ProductPage.COMPARE_LINK)
        assert compare_link.text == f"Product Compare ({item_count})"
