from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_admin_page_visibility(browser):
    """Checking of availability of admin page"""
    browser.get(f"{browser.url}admin")
    label_username = browser.find_element_by_css_selector("label[for='input-username']")
    label_password = browser.find_element_by_css_selector("label[for='input-password']")
    login_button = browser.find_element_by_css_selector("button[type='submit']")
    label_username.is_displayed()
    label_password.is_displayed()
    login_button.is_displayed()


def test_login_inside_admin_panel(browser):
    """Checking logging functionality to the admin panel"""
    browser.get(f"{browser.url}admin")
    wait = WebDriverWait(browser, 5)
    assert browser.title == "Administration"
    username_field = browser.find_element_by_css_selector("#input-username")
    password_field = browser.find_element_by_css_selector("#input-password")
    username_field.clear()
    username_field.send_keys("demo")
    password_field.clear()
    password_field.send_keys("demo")
    browser.find_element_by_css_selector("button[type='submit']").click()
    wait.until(EC.title_is("Dashboard"))
    assert browser.title == "Dashboard"
