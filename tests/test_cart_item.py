import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

CART_ITEM_URL = "/index.php?route=product/product&path=57&product_id=49"


@pytest.mark.parametrize('device_title,product_code,reward_points,availability',
                         [('Samsung Galaxy Tab 10.1', 'SAM1', '1000', 'Pre-Order')])
def test_item_title_and_info_correctness(browser, device_title, product_code, reward_points, availability):
    """Checking title of item 'Samsung Galaxy Tab 10.1'"""
    browser.get(f"{browser.url}{CART_ITEM_URL}")
    actual_item_title = browser.find_element_by_xpath("//a[contains(text(),'Samsung Galaxy Tab 10.1')]")
    actual_product_code = browser.find_element_by_xpath("//li[contains(text(),'Product Code: SAM1')]")
    actual_reward_point = browser.find_element_by_xpath("//li[contains(text(),'Reward Points: 1000')]")
    actual_availability = browser.find_element_by_xpath("//li[contains(text(),'Availability: Pre-Order')]")

    assert actual_product_code.text.split(":")[1].replace(" ", "") == product_code
    assert actual_reward_point.text.split(":")[1].replace(" ", "") == reward_points
    assert actual_availability.text.split(":")[1].replace(" ", "") == availability
    assert actual_item_title.text == device_title


def test_add_item_to_the_cart(browser):
    """Checking of adding item to the cart and check success message"""
    browser.get(f"{browser.url}{CART_ITEM_URL}")
    wait = WebDriverWait(browser, 5)
    button_add_cart = browser.find_element_by_css_selector("#button-cart")
    button_add_cart.click()
    assert button_add_cart.text == "Loading..."
    success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.alert")))
    assert success_message.text[:-2] == "Success: You have added Samsung Galaxy Tab 10.1 to your shopping cart!"


@pytest.mark.parametrize('expected_price,expected_tax', [('$241.99', '$199.99')])
def test_check_item_price(browser, expected_price, expected_tax):
    """Checking prices and taxes of item"""
    browser.get(f"{browser.url}{CART_ITEM_URL}")
    actual_item_price = browser.find_element_by_css_selector("div.col-sm-4 ul.list-unstyled h2")
    actual_tax = browser.find_element_by_xpath("//li[contains(text(),'Ex Tax')]")
    assert actual_tax.text.split(":")[1].replace(" ", "") == expected_tax
    assert actual_item_price.text == expected_price
