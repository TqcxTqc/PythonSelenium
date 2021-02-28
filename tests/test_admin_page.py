from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from _support.page.AdminPage import AdminPage


def test_admin_page_visibility(browser):
    """Checking of availability of admin page"""
    admin_page = AdminPage(browser)
    admin_page.open_page()
    admin_page.check_page_label_is_present(*admin_page.LABEL_USERNAME)
    admin_page.check_page_label_is_present(*admin_page.LABEL_USERNAME)


def test_login_inside_admin_panel(browser, admin_account):
    """Checking logging functionality to the admin panel"""
    wait = WebDriverWait(browser, 5)
    admin_page = AdminPage(browser)
    admin_page.open_page()
    assert browser.title == "Administration"

    admin_page.sign_in_admin_panel(admin_account['username'], admin_account['password'])
    wait.until(EC.title_is("Dashboard"))
    assert browser.title == "Dashboard"


def test_check_orders(browser, admin_account):
    """Checking Sales order items"""
    wait = WebDriverWait(browser, 5)
    admin_page = AdminPage(browser)
    admin_page.open_page()
    assert browser.title == "Administration"

    admin_page.sign_in_admin_panel(admin_account['username'], admin_account['password'])
    wait.until(EC.title_is("Dashboard"))

    admin_page.navigate_to_ordes_in_sales()
    assert admin_page.get_title_page() == "Orders"
    assert admin_page.get_order_items_count() == "Showing 1 to 20 of 8269"
