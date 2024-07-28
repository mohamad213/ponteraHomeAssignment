from playwright.sync_api import Page
from . import NewClientPageLocators


class NewClientPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = NewClientPageLocators.TITLE
        self.first_name = NewClientPageLocators.FIRST_NAME
        self.last_name = NewClientPageLocators.LAST_NAME
        self.add_client_button = NewClientPageLocators.ADD_CLIENT_BUTTON

    def is_page_loaded(self):
        return ((self.page.is_visible(self.title) &
                self.page.is_visible(self.first_name) &
                self.page.is_visible(self.last_name) &
                self.page.is_visible(self.add_client_button)) &
                ("edit" in self.page.url))
