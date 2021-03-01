from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from _support.page import LoginPage


def test_presents_of_login_page(browser):
    """Checking correctness of login table"""
    login_page = LoginPage(browser)
    login_page.open_page()
    login_page.open_login()
    # browser.find_element_by_css_selector("a[title='My Account']").click()
    # browser.find_element_by_xpath("//a[normalize-space()='Login']").click()
    # page_title = browser.title
    # assert page_title == "Account Login"
    # login_customer_table = browser.find_element_by_css_selector("div.col-sm-6:nth-child(2)")
    # title_table = login_customer_table.find_element_by_css_selector("h2")
    # email_field = login_customer_table.find_element_by_id("input-email")
    # password_field = login_customer_table.find_element_by_id("input-password")
    # forgot_password = login_customer_table.find_element_by_link_text("Forgotten Password")
    # title_table.is_displayed()
    # email_field.is_displayed()
    # password_field.is_displayed()
    # forgot_password.is_displayed()


def test_error_alert_login(browser):
    """Checking alert message with empty values"""
    browser.get(browser.url)
    wait = WebDriverWait(browser, 5)
    browser.find_element_by_css_selector("a[title='My Account']").click()
    browser.find_element_by_xpath("//a[normalize-space()='Login']").click()
    login_customer_table = browser.find_element_by_css_selector("div.col-sm-6:nth-child(2)")
    login_customer_table.find_element_by_css_selector("input[value='Login']").click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")))
    alert_message = browser.find_element_by_xpath("//div[@class='alert alert-danger alert-dismissible']")
    assert alert_message.text == "Warning: No match for E-Mail Address and/or Password."
