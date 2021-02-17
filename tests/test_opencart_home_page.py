import pytest


def test_checking_logo(browser):
    """Checking presentation of logo with correct URL and text of logo"""
    browser.get(browser.url)
    logo_text = browser.find_element_by_css_selector("#logo").get_property("outerText")
    logo_url = browser.find_element_by_css_selector("#logo").get_property("baseURI")
    assert logo_url == "https://demo.opencart.com/"
    assert logo_text == "Your Store"


@pytest.mark.parametrize('expected_items', [['MacBook', 'iPhone', 'Apple Cinema 30"', 'Canon EOS 5D']])
def test_check_featured_items(browser, expected_items):
    """Checking feature items presented on home page"""
    browser.get(browser.url)
    featured_item_head = browser.find_element_by_css_selector("#content > h3").text
    featured_items = browser.find_elements_by_css_selector(".product-layout .caption h4")
    get_all_items = []

    for item in featured_items:
        get_all_items.append(item.text)

    assert get_all_items == expected_items
    assert featured_item_head == "Featured"


@pytest.mark.parametrize('expected_information,expected_customer_service,expected_extras,expected_my_account',
                         [(
                                 ['About Us', 'Delivery', 'Information', 'Privacy', 'Policy,Terms & Conditions'],
                                 ['Contact Us', 'Returns', 'Site Map'],
                                 ['Brands', 'Gift Certificates', 'Affiliate,Specials'],
                                 ['My Account', 'Order History', 'Wish List', 'Newsletter']
                         )],
                         ids=['Information', 'Customer_service', 'Extras', 'My_account'])
@pytest.mark.parametrize('expected_footer_titles', [['Information', 'Customer Service', 'Extras', 'My Account']])
def test_check_main_page_footer(browser, expected_information, expected_customer_service, expected_extras,
                                expected_my_account, expected_footer_titles):
    browser.get(browser.url)
    get_footer_titles = browser.find_elements_by_css_selector('footer .col-sm-3 h5')
    actual_footer_title = []

    for text_in_items in get_footer_titles:
        actual_footer_title.append(text_in_items.text)

    assert actual_footer_title == expected_footer_titles
