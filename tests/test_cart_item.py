import pytest

CART_ITEM_URL = "index.php?route=product/product&path=57&product_id=49"


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
