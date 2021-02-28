import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

CATALOGUE_URL = "/index.php?route=product/category&path=20"


@pytest.mark.parametrize('expected_item_titles',
                         [['Apple Cinema 30"', 'Canon EOS 5D', 'HP LP3065', 'HTC Touch HD',
                           'iPhone', 'iPod Classic', 'MacBook', 'MacBook Air', 'Palm Treo Pro',
                           'Product 8', 'Samsung SyncMaster 941BW', 'Sony VAIO']])
def test_desktops_catalogue(browser, expected_item_titles):
    """Checking desktops products from catalogue page"""
    browser.get(f"{browser.url}{CATALOGUE_URL}")
    get_items_titles = browser.find_elements_by_css_selector(".caption a")
    actual_titles = []

    for item in get_items_titles:
        actual_titles.append(item.text)

    assert actual_titles == expected_item_titles


def test_desktop_filter(browser):
    """Checking filter for desktops products by Mac"""
    browser.get(f"{browser.url}{CATALOGUE_URL}")
    wait = WebDriverWait(browser, 5)
    left_menu = browser.find_element_by_css_selector("#column-left")
    mac_item = left_menu.find_element_by_css_selector(".list-group-item:nth-child(3)")

    mac_item.click()
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".caption h4"), "iMac"))


def test_add_comparison_products(browser):
    """Checking of adding product in to link 'Product Compare'"""
    browser.get(f"{browser.url}{CATALOGUE_URL}")
    wait = WebDriverWait(browser, 5)
    random_item = random.randint(1, 5)
    product_compare_link = browser.find_element_by_id("compare-total")

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, f"(//div[@class='button-group']/button[contains(@onclick,'compare.add')])[{random_item}]"))).click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))

    assert product_compare_link.text == "Product Compare (1)"
