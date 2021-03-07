import pytest
from _support.page import HomePage


def test_checking_logo(browser):
    """Checking presentation of logo with correct URL and text of logo"""
    home_page = HomePage(browser)
    home_page.open_page()
    home_page.check_home_page_logo()


@pytest.mark.parametrize('expected_items', [['MacBook', 'iPhone', 'Apple Cinema 30"', 'Canon EOS 5D']])
def test_check_featured_items(browser, expected_items):
    """Checking feature items presented on home page"""
    home_page = HomePage(browser)
    home_page.open_page()
    home_page.check_feature_items(expected_items)


@pytest.mark.parametrize('expected_footer_data',
                         [[
                             ['Information, About Us, Delivery Information, Privacy Policy, Terms & Conditions'],
                             ['Customer Service, Contact Us, Returns, Site Map'],
                             ['Extras, Brands, Gift Certificates, Affiliate, Specials'],
                             ['My Account, My Account, Order History, Wish List, Newsletter']
                         ]])
def test_check_main_page_footer(browser, expected_footer_data):
    """Checking main page footer for correctness of sub-links"""
    home_page = HomePage(browser)
    home_page.open_page()
    home_page.check_footer(expected_footer_data)


@pytest.mark.parametrize('expected_menu_items', [
    ['Desktops, Laptops & Notebooks, Components, Tablets, Software, Phones & PDAs, Cameras, MP3 Players']])
def test_check_store_menu(browser, expected_menu_items):
    """Checking main menu list of items"""
    home_page = HomePage(browser)
    home_page.open_page()
    home_page.check_navigation_bar(expected_menu_items)
