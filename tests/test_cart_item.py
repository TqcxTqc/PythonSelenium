import pytest
import allure
from _support.page import ProductPage


@allure.title("Checking new added product information")
@allure.feature("New Product")
@pytest.mark.parametrize('device_title,product_code,reward_points,availability',
                         [('Samsung Galaxy Tab 10.1', 'SAM1', '1000', 'Pre-Order')])
def test_item_title_and_info_correctness(browser, device_title, product_code, reward_points, availability):
    """Checking title of item 'Samsung Galaxy Tab 10.1'"""
    product_page = ProductPage(browser)
    product_page.open_special_page(ProductPage.SAMSUNG_GALAXY_ITEM)
    product_page.check_product_title(device_title)
    product_page.check_product_info_data(product_code, reward_points, availability)


@allure.title("Checking adding of new product in to cart")
@allure.feature("New Product")
@pytest.mark.parametrize('product_item', ['Samsung Galaxy Tab 10.1'])
def test_add_item_to_the_cart(browser, product_item):
    """Checking of adding item to the cart and check success message"""
    product_page = ProductPage(browser)
    product_page.open_special_page(ProductPage.SAMSUNG_GALAXY_ITEM)
    product_page.add_item_to_cart()
    product_page.get_success_message(product_item)


@allure.title("Checking new item price and tax")
@allure.feature("New Product")
@allure.issue(name="Failed by prices", url="LINK TO URL")
@pytest.mark.parametrize('expected_price,expected_tax', [('$241.99', '$199.99')])
def test_check_item_price(browser, expected_price, expected_tax):
    """Checking prices and taxes of item"""
    product_page = ProductPage(browser)
    product_page.open_special_page("/index.php?route=product/product&path=18&product_id=43")
    product_page.get_product_price(expected_price, expected_tax)
