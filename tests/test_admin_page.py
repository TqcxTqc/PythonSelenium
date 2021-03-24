import allure
from _support.page.AdminPage import AdminPage


@allure.title("Checking visibility of admin page")
def test_admin_page_visibility(browser):
    """Checking of availability of admin page"""
    admin_page = AdminPage(browser)
    admin_page.open_special_page(admin_page.ADMIN_URL)
    admin_page.check_page_element_is_present(*admin_page.LABEL_USERNAME)
    admin_page.check_page_element_is_present(*admin_page.LABEL_USERNAME)

@allure.feature("Authorization")
@allure.story("Admin authorization")
@allure.title("Checking login in to admin page")
def test_login_inside_admin_panel(browser, admin_account):
    """Checking logging functionality to the admin panel"""
    admin_page = AdminPage(browser)
    admin_page.open_special_page(admin_page.ADMIN_URL)
    assert browser.title == "Administration"
    admin_page.sign_in_admin_panel(admin_account['username'], admin_account['password'])
    assert browser.title == "Dashboard"


@allure.title("Checking orders in admin page")
def test_check_orders(browser, admin_account):
    """Checking Sales order items"""
    admin_page = AdminPage(browser)
    admin_page.open_special_page(admin_page.ADMIN_URL)
    assert browser.title == "Administration"
    admin_page.sign_in_admin_panel(admin_account['username'], admin_account['password'])
    admin_page.navigate_to_ordes_in_sales()
    assert admin_page.get_title_page() == "Orders"
    assert admin_page.get_order_items_count() == "Showing 1 to 20 of 8271"
