from selenium.webdriver.common.by import By
from .BasePage import BasePage


class HomePage(BasePage):
    FEATURED_TITLE = (By.CSS_SELECTOR, "#content > h3")
    FEATURED_ITEMS = (By.CSS_SELECTOR, ".caption h4")

    def check_feature_items(self, items):
        featured_items = self.browser.find_elements(*HomePage.FEATURED_ITEMS)
        get_all_items = []

        for item in featured_items:
            get_all_items.append(item.text)

        assert get_all_items == items
        assert self.browser.find_element(*HomePage.FEATURED_TITLE).text == "Featured"

    def check_home_page_logo(self):
        self.top_menu.top_menu_logo()

    def check_footer(self, footer_columns):
        footer = self.footer.get_footer()
        actual_footer_column_data = []

        for item in range(len(footer)):
            raw_list = []
            raw_list.append(footer[item].text.replace("\n", ", "))
            actual_footer_column_data.append(raw_list)

        for item_column in range(len(actual_footer_column_data)):
            assert actual_footer_column_data[item_column] == footer_columns[item_column]

    def check_navigation_bar(self, menu_items):
        item_in_menu = self.top_menu.top_navigation_bar()
        actual_menu_of_items = []
        actual_menu_of_items.append(item_in_menu.text.replace("\n", ", "))
        assert actual_menu_of_items == menu_items
