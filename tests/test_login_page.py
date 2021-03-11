from _support.page import LoginPage


def test_presents_of_login_page(browser):
    """Checking correctness of login table"""
    login_page = LoginPage(browser)
    login_page.open_page()
    login_page.open_login()
    page_title = browser.title
    assert page_title == "Account Login"
    login_page.check_page()


def test_error_alert_login(browser):
    """Checking alert message with empty values"""
    login_page = LoginPage(browser)
    login_page.open_page()
    login_page.open_login()
    login_page.click_login_button()
    alert_message = login_page.wait_error_alert()
    assert alert_message.text == "Warning: No match for E-Mail Address and/or Password."
