from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_admin_page_visibility(browser):
    """Checking of availability of admin page"""
    browser.get(f"{browser.url}/admin")
    label_username = browser.find_element_by_css_selector("label[for='input-username']")
    label_password = browser.find_element_by_css_selector("label[for='input-password']")
    login_button = browser.find_element_by_css_selector("button[type='submit']")
    label_username.is_displayed()
    label_password.is_displayed()
    login_button.is_displayed()


def test_login_inside_admin_panel(browser, admin_account):
    """Checking logging functionality to the admin panel"""
    browser.get(f"{browser.url}/admin")
    wait = WebDriverWait(browser, 5)
    assert browser.title == "Administration"
    username_field = browser.find_element_by_css_selector("#input-username")
    password_field = browser.find_element_by_css_selector("#input-password")
    username_field.clear()
    username_field.send_keys(admin_account['username'])
    password_field.clear()
    password_field.send_keys(admin_account['password'])
    browser.find_element_by_css_selector("button[type='submit']").click()
    wait.until(EC.title_is("Dashboard"))
    assert browser.title == "Dashboard"


def test_check_orders(browser, admin_account):
    """Checking Sales order items"""
    browser.get(f"{browser.url}/admin")
    wait = WebDriverWait(browser, 5)

    assert browser.title == "Administration"
    username_field = browser.find_element_by_css_selector("#input-username")
    password_field = browser.find_element_by_css_selector("#input-password")
    username_field.clear()
    username_field.send_keys(admin_account["username"])
    password_field.clear()
    password_field.send_keys(admin_account["password"])
    browser.find_element_by_css_selector("button[type='submit']").click()
    wait.until(EC.title_is("Dashboard"))

    browser.find_element_by_xpath("//a[contains(text(),'Sales')]").click()
    browser.find_element_by_xpath("//a[contains(text(),'Orders')]").click()
    orders_title = browser.find_element_by_css_selector(".container-fluid h1")
    assert orders_title.text == "Orders"
    showing_items_text = browser.find_element_by_xpath("//div[@class='col-sm-6 text-right']")
    assert showing_items_text.text[:-12] == "Showing 1 to 20 of 8259"
