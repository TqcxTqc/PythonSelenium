import pytest
import allure
import random
from _support.page import ProductPage


@allure.title("Checking catalogue on page")
@pytest.mark.parametrize('expected_item_titles',
                         [['Apple Cinema 30"', 'Canon EOS 5D', 'HP LP3065', 'HTC Touch HD',
                           'iPhone', 'iPod Classic', 'MacBook', 'MacBook Air', 'Palm Treo Pro',
                           'Product 8', 'Samsung SyncMaster 941BW', 'Sony VAIO']])
def test_desktops_catalogue(browser, expected_item_titles):
    """Checking desktops products from catalogue page"""
    product_page = ProductPage(browser)
    product_page.open_special_page(ProductPage.CATALOGUE_URL)
    product_page.get_all_items_title_on_page(expected_item_titles)


@allure.title("Checking filter,filtering by MAC product")
def test_desktop_filter(browser):
    """Checking filter for desktops products by Mac"""
    product_page = ProductPage(browser)
    product_page.open_special_page(ProductPage.CATALOGUE_URL)
    product_page.select_item_in_left_menu('Mac')
    product_page.check_item_to_be_present('iMac')


@allure.title("Adding product to comparison link ")
def test_add_comparison_products(browser):
    """Checking of adding product in to link 'Product Compare'"""
    product_page = ProductPage(browser)
    product_page.open_special_page(ProductPage.CATALOGUE_URL)
    random_item = random.randint(1, 5)
    product_page.check_compare_link(0)
    product_page.click_comparison_button(random_item)
    product_page.check_compare_link(1)
